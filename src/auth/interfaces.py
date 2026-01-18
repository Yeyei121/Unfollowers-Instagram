"""
Interfaces para el módulo de autenticación.
Siguiendo el principio de Inversión de Dependencias (SOLID).
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import instaloader


class IAuthenticationProvider(ABC):
    """
    Interfaz para proveedores de autenticación.
    Permite diferentes métodos de autenticación (cookies, sesión guardada, etc.).
    """
    
    @abstractmethod
    def authenticate(self) -> bool:
        """
        Realiza la autenticación.
        
        Returns:
            bool: True si la autenticación fue exitosa, False en caso contrario.
        """
        pass
    
    @abstractmethod
    def get_loader(self) -> Optional[instaloader.Instaloader]:
        """
        Obtiene la instancia de Instaloader autenticada.
        
        Returns:
            Optional[Instaloader]: Instancia de Instaloader o None si no está autenticado.
        """
        pass
    
    @abstractmethod
    def get_username(self) -> Optional[str]:
        """
        Obtiene el nombre de usuario autenticado.
        
        Returns:
            Optional[str]: Nombre de usuario o None si no está autenticado.
        """
        pass
    
    @abstractmethod
    def is_authenticated(self) -> bool:
        """
        Verifica si hay una sesión autenticada activa.
        
        Returns:
            bool: True si está autenticado, False en caso contrario.
        """
        pass


class ISessionManager(ABC):
    """
    Interfaz para gestores de sesión.
    Maneja la persistencia y recuperación de sesiones.
    """
    
    @abstractmethod
    def save_session(self, username: str, session_data: Any) -> bool:
        """
        Guarda una sesión en el almacenamiento.
        
        Args:
            username: Nombre de usuario de la sesión.
            session_data: Datos de la sesión a guardar.
            
        Returns:
            bool: True si se guardó exitosamente, False en caso contrario.
        """
        pass
    
    @abstractmethod
    def load_session(self, username: str) -> Optional[Any]:
        """
        Carga una sesión desde el almacenamiento.
        
        Args:
            username: Nombre de usuario de la sesión a cargar.
            
        Returns:
            Optional[Any]: Datos de la sesión o None si no existe.
        """
        pass
    
    @abstractmethod
    def session_exists(self, username: str) -> bool:
        """
        Verifica si existe una sesión guardada para un usuario.
        
        Args:
            username: Nombre de usuario a verificar.
            
        Returns:
            bool: True si existe la sesión, False en caso contrario.
        """
        pass
    
    @abstractmethod
    def delete_session(self, username: str) -> bool:
        """
        Elimina una sesión guardada.
        
        Args:
            username: Nombre de usuario de la sesión a eliminar.
            
        Returns:
            bool: True si se eliminó exitosamente, False en caso contrario.
        """
        pass
