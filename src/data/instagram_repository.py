"""
Implementación del repositorio de Instagram usando Instaloader.
"""

import instaloader
from typing import Set, Dict, Any, Optional
from .interfaces import IInstagramRepository
from ..auth.interfaces import IAuthenticationProvider


class InstagramRepository(IInstagramRepository):
    """
    Repositorio de datos de Instagram.
    Implementa el patrón Repository para encapsular la lógica de acceso a datos.
    Siguiendo Dependency Inversion Principle: depende de IAuthenticationProvider.
    """
    
    def __init__(self, auth_provider: IAuthenticationProvider):
        """
        Inicializa el repositorio con un proveedor de autenticación.
        
        Args:
            auth_provider: Proveedor de autenticación que proporciona el loader.
        """
        if not auth_provider.is_authenticated():
            raise ValueError("El proveedor de autenticación debe estar autenticado")
        
        self._auth_provider = auth_provider
        self._loader = auth_provider.get_loader()
        self._username = auth_provider.get_username()
    
    def get_followers(self, username: Optional[str] = None) -> Set[str]:
        """
        Obtiene la lista de seguidores de un usuario.
        
        Args:
            username: Nombre de usuario. Si es None, usa el usuario autenticado.
            
        Returns:
            Set[str]: Conjunto de nombres de usuario de los seguidores.
        """
        target_username = username or self._username
        
        if not target_username:
            raise ValueError("No hay usuario especificado")
        
        try:
            print(f"\n📥 Obteniendo seguidores de @{target_username}...")
            profile = instaloader.Profile.from_username(
                self._loader.context,
                target_username
            )
            
            followers = set()
            count = 0
            
            for follower in profile.get_followers():
                followers.add(follower.username)
                count += 1
                if count % 50 == 0:
                    print(f"   Procesados {count} seguidores...")
            
            print(f"✓ Total de seguidores: {len(followers)}")
            return followers
            
        except instaloader.exceptions.ProfileNotExistsException:
            raise ValueError(f"El perfil @{target_username} no existe")
        except instaloader.exceptions.LoginRequiredException:
            raise PermissionError("Se requiere autenticación para acceder a esta información")
        except Exception as e:
            raise Exception(f"Error al obtener seguidores: {e}")
    
    def get_following(self, username: Optional[str] = None) -> Set[str]:
        """
        Obtiene la lista de usuarios seguidos por un usuario.
        
        Args:
            username: Nombre de usuario. Si es None, usa el usuario autenticado.
            
        Returns:
            Set[str]: Conjunto de nombres de usuario seguidos.
        """
        target_username = username or self._username
        
        if not target_username:
            raise ValueError("No hay usuario especificado")
        
        try:
            print(f"\n📤 Obteniendo seguidos de @{target_username}...")
            profile = instaloader.Profile.from_username(
                self._loader.context,
                target_username
            )
            
            following = set()
            count = 0
            
            for followee in profile.get_followees():
                following.add(followee.username)
                count += 1
                if count % 50 == 0:
                    print(f"   Procesados {count} seguidos...")
            
            print(f"✓ Total de seguidos: {len(following)}")
            return following
            
        except instaloader.exceptions.ProfileNotExistsException:
            raise ValueError(f"El perfil @{target_username} no existe")
        except instaloader.exceptions.LoginRequiredException:
            raise PermissionError("Se requiere autenticación para acceder a esta información")
        except Exception as e:
            raise Exception(f"Error al obtener seguidos: {e}")
    
    def get_profile_info(self, username: Optional[str] = None) -> Dict[str, Any]:
        """
        Obtiene información del perfil de un usuario.
        
        Args:
            username: Nombre de usuario. Si es None, usa el usuario autenticado.
            
        Returns:
            Dict[str, Any]: Información del perfil.
        """
        target_username = username or self._username
        
        if not target_username:
            raise ValueError("No hay usuario especificado")
        
        try:
            profile = instaloader.Profile.from_username(
                self._loader.context,
                target_username
            )
            
            return {
                'username': profile.username,
                'full_name': profile.full_name,
                'followers': profile.followers,
                'following': profile.followees,
                'posts': profile.mediacount,
                'is_private': profile.is_private,
                'biography': profile.biography
            }
            
        except Exception as e:
            raise Exception(f"Error al obtener información del perfil: {e}")
