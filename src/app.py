"""
Aplicación principal del analizador de Instagram.
Implementa el patrón de Fachada e inyección de dependencias.
"""

import sys
import instaloader
from pathlib import Path
from typing import Optional

from .auth import (
    IAuthenticationProvider,
    InstaloaderSessionManager,
    CookieAuthProvider,
    SavedSessionAuthProvider
)
from .data import InstagramRepository
from .analysis import FollowerAnalyzer
from .utils import FileManager, TextReportExporter, JSONReportExporter, UnfollowersListExporter
from .ui import ConsolePrinter, InputValidator, MenuManager, MenuItem


class InstagramAnalyzerApp:
    """
    Aplicación principal del analizador de seguidores de Instagram.
    Implementa el patrón Facade para simplificar la interacción con todos los módulos.
    Utiliza inyección de dependencias para cumplir con Dependency Inversion Principle.
    """
    
    def __init__(self, base_directory: Optional[Path] = None):
        """
        Inicializa la aplicación.
        
        Args:
            base_directory: Directorio base de trabajo.
        """
        self.base_directory = base_directory or Path.cwd()
        
        # Inicializar componentes
        self._session_manager = InstaloaderSessionManager(self.base_directory)
        self._file_manager = FileManager(self.base_directory)
        self._printer = ConsolePrinter()
        self._validator = InputValidator()
        self._menu_manager = MenuManager(self._printer, self._validator)
        self._auth_provider: Optional[IAuthenticationProvider] = None
        self._repository: Optional[InstagramRepository] = None
        self._setup_menus()
    
    def _setup_menus(self):
        """Configura los menús de la aplicación."""
        # Menú principal
        main_menu_items = [
            MenuItem("Crear sesión desde cookies del navegador", self._create_session_from_cookies),
            MenuItem("Cargar sesión guardada", self._load_saved_session),
            MenuItem("Analizar seguidores", self._analyze_followers),
            MenuItem("Salir", lambda: None)
        ]
        self._menu_manager.register_menu("main", main_menu_items)
        
        # Menú de exportación
        export_menu_items = [
            MenuItem("Exportar reporte completo (TXT)", self._export_text_report),
            MenuItem("Exportar reporte completo (JSON)", self._export_json_report),
            MenuItem("Exportar solo lista de unfollowers", self._export_unfollowers_list),
            MenuItem("No exportar", lambda: None)
        ]
        self._menu_manager.register_menu("export", export_menu_items)
    
    def run(self):
        """Ejecuta la aplicación principal."""
        try:
            self._printer.print_header("📱 ANALIZADOR DE SEGUIDORES DE INSTAGRAM")
            self._printer.print_info("Aplicación para analizar quién te dejó de seguir en Instagram\n")
            
            while True:
                option = self._menu_manager.show_menu("main", "🔐 MENÚ PRINCIPAL")
                
                if option is None or option == 4:
                    self._printer.print_success("¡Hasta pronto!")
                    break
                
                self._menu_manager.execute_menu_option("main", option)
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario")
        except Exception as e:
            self._printer.print_error(f"Error inesperado: {e}")
            import traceback
            traceback.print_exc()
    
    def _create_session_from_cookies(self):
        """Crea una sesión desde cookies del navegador."""
        self._printer.print_cookie_instructions()
        
        # Solicitar credenciales
        username = self._validator.get_non_empty_string("👤 Usuario de Instagram: ")
        if not username:
            return
        
        sessionid = self._validator.get_non_empty_string("🔑 SessionID: ")
        if not sessionid:
            return
        try:
            self._printer.print_section("\n🔐 Autenticando...")
            
            auth_provider = CookieAuthProvider(self._session_manager, username, sessionid)
            
            if auth_provider.authenticate():
                self._auth_provider = auth_provider
                
                # Verificar sesión
                loader = auth_provider.get_loader()
                profile = instaloader.Profile.from_username(loader.context, username)
                
                self._printer.print_verification_message(
                    username,
                    profile.followers,
                    profile.followees
                )
                
                # Crear repositorio
                self._repository = InstagramRepository(auth_provider)
                
                self._printer.print_success("Sesión creada y guardada exitosamente")
            else:
                self._printer.print_error("No se pudo autenticar. Verifica tus credenciales.")
                
        except Exception as e:
            self._printer.print_error(f"Error al crear sesión: {e}")
            self._auth_provider = None
            self._repository = None
    
    def _load_saved_session(self):
        """Carga una sesión guardada."""
        username = self._validator.get_non_empty_string("\n👤 Usuario de la sesión guardada: ")
        if not username:
            return
        
        try:
            self._printer.print_section("\n🔐 Cargando sesión...")
            
            auth_provider = SavedSessionAuthProvider(self._session_manager, username)
            
            if auth_provider.authenticate():
                self._auth_provider = auth_provider
                
                # Verificar sesión
                loader = auth_provider.get_loader()
                profile = instaloader.Profile.from_username(loader.context, username)
                
                self._printer.print_verification_message(
                    username,
                    profile.followers,
                    profile.followees
                )
                
                # Crear repositorio
                self._repository = InstagramRepository(auth_provider)
                
                self._printer.print_success("Sesión cargada exitosamente")
            else:
                self._printer.print_error("No se pudo cargar la sesión.")
                
        except Exception as e:
            self._printer.print_error(f"Error al cargar sesión: {e}")
            self._auth_provider = None
            self._repository = None
    
    def _analyze_followers(self):
        """Analiza los seguidores del usuario autenticado."""
        if not self._auth_provider or not self._auth_provider.is_authenticated():
            self._printer.print_error("Debes autenticarte primero (opción 1 o 2)")
            return
        
        if not self._repository:
            self._printer.print_error("Error: repositorio no inicializado")
            return
        
        try:
            self._printer.print_warning("El proceso puede tardar varios minutos...")
            self._printer.print_info("Instagram limita la velocidad de las solicitudes\n")
            
            if not self._validator.get_yes_no_confirmation("¿Deseas continuar?", default=True):
                return
            
            username = self._auth_provider.get_username()
            self._printer.print_section(f"\n📊 Analizando cuenta @{username}...")
            
            # Obtener datos
            followers = self._repository.get_followers()
            following = self._repository.get_following()
            
            if not followers and not following:
                self._printer.print_error("No se pudieron obtener los datos")
                return
            
            # Realizar análisis
            self._printer.print_section("\n🔍 Analizando datos...")
            analyzer = FollowerAnalyzer(followers, following)
            result = analyzer.analyze()
            
            # Mostrar resumen
            self._printer.print_analysis_summary(result)
            
            # Guardar resultado para exportación
            self._last_analysis_result = result
            
            # Preguntar si desea exportar
            print("")
            if self._validator.get_yes_no_confirmation("¿Deseas exportar los resultados?", default=True):
                self._show_export_menu()
            
            self._printer.print_success("\nAnálisis completado exitosamente!")
            
        except Exception as e:
            self._printer.print_error(f"Error durante el análisis: {e}")
            import traceback
            traceback.print_exc()
    
    def _show_export_menu(self):
        """Muestra el menú de exportación."""
        option = self._menu_manager.show_menu("export", "\n💾 ¿QUÉ DESEAS EXPORTAR?")
        
        if option and option != 4:
            self._menu_manager.execute_menu_option("export", option)
    
    def _export_text_report(self):
        """Exporta el reporte en formato texto."""
        if not hasattr(self, '_last_analysis_result'):
            self._printer.print_error("No hay análisis disponible para exportar")
            return
        
        exporter = TextReportExporter(self._file_manager)
        exporter.export(self._last_analysis_result)
    
    def _export_json_report(self):
        """Exporta el reporte en formato JSON."""
        if not hasattr(self, '_last_analysis_result'):
            self._printer.print_error("No hay análisis disponible para exportar")
            return
        
        exporter = JSONReportExporter(self._file_manager)
        exporter.export(self._last_analysis_result)
    
    def _export_unfollowers_list(self):
        """Exporta solo la lista de unfollowers."""
        if not hasattr(self, '_last_analysis_result'):
            self._printer.print_error("No hay análisis disponible para exportar")
            return
        
        exporter = UnfollowersListExporter(self._file_manager)
        exporter.export(self._last_analysis_result.not_following_back)
