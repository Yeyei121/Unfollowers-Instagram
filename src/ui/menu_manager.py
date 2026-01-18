"""
Gestor de menús.
"""

from typing import Callable, List, Dict, Optional
from .console_printer import ConsolePrinter
from .input_validator import InputValidator


class MenuItem:
    """
    Representa un elemento de menú.
    """
    
    def __init__(self, label: str, action: Callable[[], None]):
        """
        Inicializa un elemento de menú.
        
        Args:
            label: Etiqueta a mostrar.
            action: Función a ejecutar cuando se selecciona.
        """
        self.label = label
        self.action = action


class MenuManager:
    """
    Gestor de menús interactivos.
    Siguiendo Single Responsibility Principle: solo gestiona menús.
    """
    
    def __init__(self, printer: ConsolePrinter, validator: InputValidator):
        """
        Inicializa el gestor de menús.
        
        Args:
            printer: Impresora de consola.
            validator: Validador de entradas.
        """
        self._printer = printer
        self._validator = validator
        self._menus: Dict[str, List[MenuItem]] = {}
    
    def register_menu(self, menu_id: str, items: List[MenuItem]):
        """
        Registra un menú.
        
        Args:
            menu_id: Identificador del menú.
            items: Lista de elementos del menú.
        """
        self._menus[menu_id] = items
    
    def show_menu(self, menu_id: str, title: str) -> Optional[int]:
        """
        Muestra un menú y obtiene la selección del usuario.
        
        Args:
            menu_id: Identificador del menú.
            title: Título del menú.
            
        Returns:
            Optional[int]: Opción seleccionada o None si se cancela.
        """
        if menu_id not in self._menus:
            raise ValueError(f"Menú '{menu_id}' no registrado")
        
        items = self._menus[menu_id]
        
        self._printer.print_section(title)
        
        options = [item.label for item in items]
        self._printer.print_options(options)
        
        return self._validator.get_valid_option(
            "\nSelecciona una opción: ",
            1,
            len(items)
        )
    
    def execute_menu_option(self, menu_id: str, option: int) -> bool:
        """
        Ejecuta la acción de una opción del menú.
        
        Args:
            menu_id: Identificador del menú.
            option: Número de opción (1-indexed).
            
        Returns:
            bool: True si se ejecutó correctamente.
        """
        if menu_id not in self._menus:
            return False
        
        items = self._menus[menu_id]
        
        if 1 <= option <= len(items):
            items[option - 1].action()
            return True
        
        return False
    
    def run_menu_loop(self, menu_id: str, title: str) -> bool:
        """
        Ejecuta un bucle de menú hasta que el usuario seleccione salir.
        La última opción del menú debe ser la opción de salida.
        
        Args:
            menu_id: Identificador del menú.
            title: Título del menú.
            
        Returns:
            bool: True si se completó normalmente.
        """
        if menu_id not in self._menus:
            raise ValueError(f"Menú '{menu_id}' no registrado")
        
        items = self._menus[menu_id]
        exit_option = len(items)
        
        while True:
            option = self.show_menu(menu_id, title)
            
            if option is None:
                return False
            
            if option == exit_option:
                return True
            
            self.execute_menu_option(menu_id, option)
