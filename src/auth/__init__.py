"""
Módulo de autenticación para Instagram.
Proporciona interfaces y clases para gestionar sesiones de Instagram.
"""

from .interfaces import IAuthenticationProvider, ISessionManager
from .session_manager import InstaloaderSessionManager
from .cookie_provider import CookieAuthProvider, BrowserCookieExtractor, SavedSessionAuthProvider

__all__ = [
    'IAuthenticationProvider',
    'ISessionManager',
    'InstaloaderSessionManager',
    'CookieAuthProvider',
    'BrowserCookieExtractor',
    'SavedSessionAuthProvider'
]
