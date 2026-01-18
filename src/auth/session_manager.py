"""
Implementación del gestor de sesiones usando Instaloader.
"""

import instaloader
from pathlib import Path
from typing import Optional, Any
from .interfaces import ISessionManager


class InstaloaderSessionManager(ISessionManager):
    """
    Gestor de sesiones utilizando el sistema de archivos de Instaloader.
    Implementa Single Responsibility Principle: solo maneja la persistencia de sesiones.
    """
    
    def __init__(self, session_directory: Optional[Path] = None):
        """
        Inicializa el gestor de sesiones.
        
        Args:
            session_directory: Directorio donde guardar las sesiones.
                              Por defecto usa el directorio actual.
        """
        self.session_directory = session_directory or Path.cwd()
        self.loader = instaloader.Instaloader()
    
    def save_session(self, username: str, session_data: Any = None) -> bool:
        """
        Guarda una sesión de Instaloader.
        
        Args:
            username: Nombre de usuario de la sesión.
            session_data: Instancia de Instaloader con la sesión activa.
            
        Returns:
            bool: True si se guardó exitosamente.
        """
        try:
            if session_data and isinstance(session_data, instaloader.Instaloader):
                loader = session_data
            else:
                loader = self.loader
            
            session_file = self.session_directory / username
            loader.save_session_to_file(str(session_file))
            return True
        except Exception as e:
            print(f"Error al guardar sesión: {e}")
            return False
    
    def load_session(self, username: str) -> Optional[instaloader.Instaloader]:
        """
        Carga una sesión guardada de Instaloader.
        
        Args:
            username: Nombre de usuario de la sesión.
            
        Returns:
            Optional[Instaloader]: Instancia de Instaloader con la sesión cargada.
        """
        try:
            loader = instaloader.Instaloader()
            session_file = self.session_directory / username
            loader.load_session_from_file(username, str(session_file))
            return loader
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error al cargar sesión: {e}")
            return None
    
    def session_exists(self, username: str) -> bool:
        """
        Verifica si existe una sesión guardada.
        
        Args:
            username: Nombre de usuario a verificar.
            
        Returns:
            bool: True si existe la sesión.
        """
        session_file = self.session_directory / username
        return session_file.exists()
    
    def delete_session(self, username: str) -> bool:
        """
        Elimina una sesión guardada.
        
        Args:
            username: Nombre de usuario de la sesión.
            
        Returns:
            bool: True si se eliminó exitosamente.
        """
        try:
            session_file = self.session_directory / username
            if session_file.exists():
                session_file.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error al eliminar sesión: {e}")
            return False
