"""
Interfaces para el módulo de datos.
"""

from abc import ABC, abstractmethod
from typing import Set, Dict, Any, Optional


class IInstagramRepository(ABC):
    """
    Interfaz para repositorio de datos de Instagram.
    Define el contrato para obtener información de Instagram.
    Siguiendo el principio de Segregación de Interfaces (SOLID).
    """
    
    @abstractmethod
    def get_followers(self, username: Optional[str] = None) -> Set[str]:
        """
        Obtiene la lista de seguidores de un usuario.
        
        Args:
            username: Nombre de usuario. Si es None, usa el usuario autenticado.
            
        Returns:
            Set[str]: Conjunto de nombres de usuario de los seguidores.
        """
        pass
    
    @abstractmethod
    def get_following(self, username: Optional[str] = None) -> Set[str]:
        """
        Obtiene la lista de usuarios seguidos por un usuario.
        
        Args:
            username: Nombre de usuario. Si es None, usa el usuario autenticado.
            
        Returns:
            Set[str]: Conjunto de nombres de usuario seguidos.
        """
        pass
    
    @abstractmethod
    def get_profile_info(self, username: Optional[str] = None) -> Dict[str, Any]:
        """
        Obtiene información del perfil de un usuario.
        
        Args:
            username: Nombre de usuario. Si es None, usa el usuario autenticado.
            
        Returns:
            Dict[str, Any]: Información del perfil.
        """
        pass
