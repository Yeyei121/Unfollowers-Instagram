"""
Modelos de datos para el análisis de seguidores.
"""

from dataclasses import dataclass
from typing import Set


@dataclass
class FollowerStatistics:
    """
    Estadísticas de seguidores.
    Inmutable para evitar modificaciones accidentales.
    """
    total_followers: int
    total_following: int
    mutual_followers: int
    not_following_back: int
    not_followed_back: int
    
    @property
    def mutual_percentage(self) -> float:
        """Porcentaje de seguidores mutuos."""
        if self.total_following == 0:
            return 0.0
        return (self.mutual_followers / self.total_following) * 100
    
    @property
    def unfollowers_percentage(self) -> float:
        """Porcentaje de usuarios que no te siguen de vuelta."""
        if self.total_following == 0:
            return 0.0
        return (self.not_following_back / self.total_following) * 100


@dataclass
class FollowerAnalysisResult:
    """
    Resultado del análisis de seguidores.
    Contiene todos los datos del análisis.
    """
    followers: Set[str]
    following: Set[str]
    mutual_followers: Set[str]
    not_following_back: Set[str]  # Te dejaron de seguir
    not_followed_back: Set[str]   # No los sigues de vuelta
    statistics: FollowerStatistics
    
    def to_dict(self) -> dict:
        """Convierte el resultado a diccionario."""
        return {
            'followers': sorted(list(self.followers)),
            'following': sorted(list(self.following)),
            'mutual_followers': sorted(list(self.mutual_followers)),
            'not_following_back': sorted(list(self.not_following_back)),
            'not_followed_back': sorted(list(self.not_followed_back)),
            'statistics': {
                'total_followers': self.statistics.total_followers,
                'total_following': self.statistics.total_following,
                'mutual_followers': self.statistics.mutual_followers,
                'not_following_back': self.statistics.not_following_back,
                'not_followed_back': self.statistics.not_followed_back,
                'mutual_percentage': self.statistics.mutual_percentage,
                'unfollowers_percentage': self.statistics.unfollowers_percentage
            }
        }
