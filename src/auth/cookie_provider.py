"""
Proveedores de autenticación basados en cookies.
"""

import json
import instaloader
from pathlib import Path
from typing import Optional, Dict
from .interfaces import IAuthenticationProvider, ISessionManager
from .session_manager import InstaloaderSessionManager


class BrowserCookieExtractor:
    """
    Clase para extraer cookies del navegador.
    Siguiendo Single Responsibility Principle: solo extrae cookies.
    """
    
    @staticmethod
    def extract_from_netscape_file(file_path: str) -> Dict[str, str]:
        """
        Extrae cookies desde un archivo en formato Netscape.
        
        Args:
            file_path: Ruta al archivo de cookies.
            
        Returns:
            Dict[str, str]: Diccionario con las cookies extraídas.
        """
        cookies = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('#') or not line.strip():
                        continue
                    
                    parts = line.strip().split('\t')
                    if len(parts) >= 7:
                        name = parts[5]
                        value = parts[6]
                        cookies[name] = value
            return cookies
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo de cookies no encontrado: {file_path}")
        except Exception as e:
            raise Exception(f"Error al leer archivo de cookies: {e}")
    
    @staticmethod
    def extract_from_json_file(file_path: str) -> Dict[str, str]:
        """
        Extrae cookies desde un archivo JSON.
        
        Args:
            file_path: Ruta al archivo JSON.
            
        Returns:
            Dict[str, str]: Diccionario con las cookies extraídas.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                cookies = json.load(f)
            return cookies
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo de cookies no encontrado: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("El archivo no es un JSON válido")
        except Exception as e:
            raise Exception(f"Error al leer archivo de cookies: {e}")
    
    @staticmethod
    def save_to_json_file(cookies: Dict[str, str], file_path: str) -> bool:
        """
        Guarda cookies en un archivo JSON.
        
        Args:
            cookies: Diccionario con las cookies.
            file_path: Ruta donde guardar el archivo.
            
        Returns:
            bool: True si se guardó exitosamente.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(cookies, f, indent=2)
            return True
        except Exception as e:
            print(f"Error al guardar cookies: {e}")
            return False


class CookieAuthProvider(IAuthenticationProvider):
    """
    Proveedor de autenticación basado en cookies.
    Implementa Dependency Inversion Principle: depende de ISessionManager.
    """
    
    def __init__(
        self,
        session_manager: ISessionManager,
        username: Optional[str] = None,
        sessionid: Optional[str] = None
    ):
        """
        Inicializa el proveedor de autenticación por cookies.
        
        Args:
            session_manager: Gestor de sesiones a utilizar.
            username: Nombre de usuario de Instagram.
            sessionid: ID de sesión de Instagram.
        """
        self._session_manager = session_manager
        self._username = username
        self._sessionid = sessionid
        self._loader: Optional[instaloader.Instaloader] = None
        self._authenticated = False
    
    def set_credentials(self, username: str, sessionid: str) -> None:
        """
        Establece las credenciales de autenticación.
        
        Args:
            username: Nombre de usuario de Instagram.
            sessionid: ID de sesión de Instagram.
        """
        self._username = username
        self._sessionid = sessionid
        self._authenticated = False
    
    def authenticate(self) -> bool:
        """
        Realiza la autenticación usando cookies.
        
        Returns:
            bool: True si la autenticación fue exitosa.
        """
        if not self._username or not self._sessionid:
            raise ValueError("Se requiere username y sessionid para autenticación")
        
        try:
            # Crear instancia de Instaloader
            self._loader = instaloader.Instaloader()
            
            # Configurar la cookie de sesión
            self._loader.context._session.cookies.set(
                'sessionid',
                self._sessionid,
                domain='.instagram.com'
            )
            self._loader.context.username = self._username
            
            # Verificar que la sesión funciona
            profile = instaloader.Profile.from_username(
                self._loader.context,
                self._username
            )
            
            # Si llegamos aquí, la autenticación fue exitosa
            self._authenticated = True
            
            # Guardar la sesión para uso futuro
            self._session_manager.save_session(self._username, self._loader)
            
            return True
            
        except Exception as e:
            print(f"Error en autenticación: {e}")
            self._authenticated = False
            self._loader = None
            return False
    
    def get_loader(self) -> Optional[instaloader.Instaloader]:
        """
        Obtiene la instancia de Instaloader autenticada.
        
        Returns:
            Optional[Instaloader]: Instancia de Instaloader o None.
        """
        return self._loader
    
    def get_username(self) -> Optional[str]:
        """
        Obtiene el nombre de usuario autenticado.
        
        Returns:
            Optional[str]: Nombre de usuario.
        """
        return self._username
    
    def is_authenticated(self) -> bool:
        """
        Verifica si hay una sesión autenticada activa.
        
        Returns:
            bool: True si está autenticado.
        """
        return self._authenticated and self._loader is not None


class SavedSessionAuthProvider(IAuthenticationProvider):
    """
    Proveedor de autenticación basado en sesiones guardadas.
    """
    
    def __init__(self, session_manager: ISessionManager, username: str):
        """
        Inicializa el proveedor de autenticación por sesión guardada.
        
        Args:
            session_manager: Gestor de sesiones.
            username: Nombre de usuario de la sesión.
        """
        self._session_manager = session_manager
        self._username = username
        self._loader: Optional[instaloader.Instaloader] = None
        self._authenticated = False
    
    def authenticate(self) -> bool:
        """
        Carga y autentica usando una sesión guardada.
        
        Returns:
            bool: True si la autenticación fue exitosa.
        """
        if not self._session_manager.session_exists(self._username):
            print(f"No existe sesión guardada para {self._username}")
            return False
        
        try:
            self._loader = self._session_manager.load_session(self._username)
            
            if not self._loader:
                return False
            
            # Verificar que la sesión sigue válida
            profile = instaloader.Profile.from_username(
                self._loader.context,
                self._username
            )
            
            self._authenticated = True
            return True
            
        except Exception as e:
            print(f"Error al cargar sesión: {e}")
            self._authenticated = False
            self._loader = None
            return False
    
    def get_loader(self) -> Optional[instaloader.Instaloader]:
        """Obtiene la instancia de Instaloader autenticada."""
        return self._loader
    
    def get_username(self) -> Optional[str]:
        """Obtiene el nombre de usuario autenticado."""
        return self._username
    
    def is_authenticated(self) -> bool:
        """Verifica si hay una sesión autenticada activa."""
        return self._authenticated and self._loader is not None
