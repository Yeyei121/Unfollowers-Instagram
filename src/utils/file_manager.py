"""
Gestor de archivos.
"""

import json
from pathlib import Path
from typing import Any, Optional


class FileManager:
    """
    Gestor de archivos.
    Siguiendo Single Responsibility Principle: solo gestiona operaciones de archivos.
    """
    
    def __init__(self, base_directory: Optional[Path] = None):
        """
        Inicializa el gestor de archivos.
        
        Args:
            base_directory: Directorio base para operaciones.
        """
        self.base_directory = base_directory or Path.cwd()
    
    def write_text_file(self, filename: str, content: str) -> bool:
        """
        Escribe contenido en un archivo de texto.
        
        Args:
            filename: Nombre del archivo.
            content: Contenido a escribir.
            
        Returns:
            bool: True si se escribió exitosamente.
        """
        try:
            file_path = self.base_directory / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error al escribir archivo {filename}: {e}")
            return False
    
    def read_text_file(self, filename: str) -> Optional[str]:
        """
        Lee contenido de un archivo de texto.
        
        Args:
            filename: Nombre del archivo.
            
        Returns:
            Optional[str]: Contenido del archivo o None si hay error.
        """
        try:
            file_path = self.base_directory / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error al leer archivo {filename}: {e}")
            return None
    
    def write_json_file(self, filename: str, data: Any) -> bool:
        """
        Escribe datos en un archivo JSON.
        
        Args:
            filename: Nombre del archivo.
            data: Datos a escribir (debe ser serializable a JSON).
            
        Returns:
            bool: True si se escribió exitosamente.
        """
        try:
            file_path = self.base_directory / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al escribir archivo JSON {filename}: {e}")
            return False
    
    def read_json_file(self, filename: str) -> Optional[Any]:
        """
        Lee datos de un archivo JSON.
        
        Args:
            filename: Nombre del archivo.
            
        Returns:
            Optional[Any]: Datos leídos o None si hay error.
        """
        try:
            file_path = self.base_directory / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            print(f"Error: {filename} no es un JSON válido")
            return None
        except Exception as e:
            print(f"Error al leer archivo JSON {filename}: {e}")
            return None
    
    def file_exists(self, filename: str) -> bool:
        """
        Verifica si un archivo existe.
        
        Args:
            filename: Nombre del archivo.
            
        Returns:
            bool: True si el archivo existe.
        """
        file_path = self.base_directory / filename
        return file_path.exists()
    
    def delete_file(self, filename: str) -> bool:
        """
        Elimina un archivo.
        
        Args:
            filename: Nombre del archivo.
            
        Returns:
            bool: True si se eliminó exitosamente.
        """
        try:
            file_path = self.base_directory / filename
            if file_path.exists():
                file_path.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error al eliminar archivo {filename}: {e}")
            return False
