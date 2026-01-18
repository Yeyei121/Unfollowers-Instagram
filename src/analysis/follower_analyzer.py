"""
Analizador de seguidores.
Implementa la lógica de análisis de seguidores vs seguidos.
"""

from typing import Set
from .models import FollowerAnalysisResult, FollowerStatistics
from .statistics_calculator import StatisticsCalculator


class FollowerAnalyzer:
    """
    Servicio para analizar seguidores y seguidos.
    Siguiendo Single Responsibility Principle: solo analiza relaciones de seguidores.
    """
    
    def __init__(self, followers: Set[str], following: Set[str]):
        """
        Inicializa el analizador.
        
        Args:
            followers: Conjunto de usuarios que te siguen.
            following: Conjunto de usuarios que sigues.
        """
        self._followers = followers
        self._following = following
        self._statistics_calculator = StatisticsCalculator()
    
    def analyze(self) -> FollowerAnalysisResult:
        """
        Realiza el análisis completo de seguidores.
        
        Returns:
            FollowerAnalysisResult: Resultado del análisis.
        """
        mutual = self._get_mutual_followers()
        not_following_back = self._get_not_following_back()
        not_followed_back = self._get_not_followed_back()
        
        # Calcular estadísticas
        statistics = self._statistics_calculator.calculate(
            total_followers=len(self._followers),
            total_following=len(self._following),
            mutual_followers=len(mutual),
            not_following_back=len(not_following_back),
            not_followed_back=len(not_followed_back)
        )
        
        return FollowerAnalysisResult(
            followers=self._followers,
            following=self._following,
            mutual_followers=mutual,
            not_following_back=not_following_back,
            not_followed_back=not_followed_back,
            statistics=statistics
        )
    
    def _get_mutual_followers(self) -> Set[str]:
        """
        Obtiene usuarios con seguimiento mutuo.
        
        Returns:
            Set[str]: Conjunto de seguidores mutuos.
        """
        return self._followers & self._following
    
    def _get_not_following_back(self) -> Set[str]:
        """
        Obtiene usuarios que sigues pero no te siguen de vuelta.
        
        Returns:
            Set[str]: Conjunto de usuarios que no te siguen.
        """
        return self._following - self._followers
    
    def _get_not_followed_back(self) -> Set[str]:
        """
        Obtiene usuarios que te siguen pero tú no sigues.
        
        Returns:
            Set[str]: Conjunto de usuarios que no sigues de vuelta.
        """
        return self._followers - self._following
