"""
Módulo de interfaz de usuario.
Proporciona componentes para la interacción con el usuario.
"""

from .menu_manager import MenuManager, MenuItem
from .console_printer import ConsolePrinter
from .input_validator import InputValidator

__all__ = [
    'MenuManager',
    'MenuItem',
    'ConsolePrinter',
    'InputValidator'
]
