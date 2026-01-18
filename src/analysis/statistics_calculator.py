"""
Calculadora de estadísticas.
"""

from .models import FollowerStatistics


class StatisticsCalculator:
    """
    Calculadora de estadísticas de seguidores.
    Siguiendo Single Responsibility Principle: solo calcula estadísticas.
    """
    
    def calculate(
        self,
        total_followers: int,
        total_following: int,
        mutual_followers: int,
        not_following_back: int,
        not_followed_back: int
    ) -> FollowerStatistics:
        """
        Calcula las estadísticas de seguidores.
        
        Args:
            total_followers: Total de seguidores.
            total_following: Total de seguidos.
            mutual_followers: Total de seguidores mutuos.
            not_following_back: Total que no te siguen de vuelta.
            not_followed_back: Total que no sigues de vuelta.
            
        Returns:
            FollowerStatistics: Estadísticas calculadas.
        """
        return FollowerStatistics(
            total_followers=total_followers,
            total_following=total_following,
            mutual_followers=mutual_followers,
            not_following_back=not_following_back,
            not_followed_back=not_followed_back
        )
