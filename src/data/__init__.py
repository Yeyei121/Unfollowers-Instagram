"""
Módulo de datos para Instagram.
Proporciona repositorios y servicios para obtener datos de Instagram.
"""

from .interfaces import IInstagramRepository
from .instagram_repository import InstagramRepository

__all__ = [
    'IInstagramRepository',
    'InstagramRepository'
]
