"""
Validador de entradas del usuario.
"""

from typing import Optional


class InputValidator:
    """
    Validador de entradas del usuario.
    Siguiendo Single Responsibility Principle: solo valida entradas.
    """
    
    @staticmethod
    def get_valid_option(prompt: str, min_option: int, max_option: int) -> Optional[int]:
        """
        Solicita y valida una opción numérica.
        
        Args:
            prompt: Mensaje a mostrar.
            min_option: Opción mínima válida.
            max_option: Opción máxima válida.
            
        Returns:
            Optional[int]: Opción válida o None si se cancela.
        """
        try:
            value = input(prompt).strip()
            
            if not value:
                return None
            
            option = int(value)
            
            if min_option <= option <= max_option:
                return option
            else:
                print(f"✗ Opción inválida. Debe estar entre {min_option} y {max_option}")
                return None
                
        except ValueError:
            print("✗ Debe ingresar un número válido")
            return None
        except KeyboardInterrupt:
            print("\n\n⚠️  Cancelado por el usuario")
            return None
    
    @staticmethod
    def get_non_empty_string(prompt: str) -> Optional[str]:
        """
        Solicita y valida una cadena no vacía.
        
        Args:
            prompt: Mensaje a mostrar.
            
        Returns:
            Optional[str]: Cadena válida o None si se cancela.
        """
        try:
            value = input(prompt).strip()
            
            if value:
                return value
            else:
                print("✗ El valor no puede estar vacío")
                return None
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Cancelado por el usuario")
            return None
    
    @staticmethod
    def get_yes_no_confirmation(prompt: str, default: bool = False) -> bool:
        """
        Solicita confirmación sí/no.
        
        Args:
            prompt: Mensaje a mostrar.
            default: Valor por defecto si se presiona Enter.
            
        Returns:
            bool: True para sí, False para no.
        """
        try:
            default_str = "S/n" if default else "s/N"
            value = input(f"{prompt} ({default_str}): ").strip().lower()
            
            if not value:
                return default
            
            return value in ['s', 'si', 'sí', 'y', 'yes']
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Cancelado por el usuario")
            return False
