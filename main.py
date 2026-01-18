"""
Punto de entrada principal de la aplicación.
Analizador de seguidores de Instagram.

Este programa te ayuda a identificar quién te dejó de seguir en Instagram.
"""

from pathlib import Path
from src.app import InstagramAnalyzerApp


def main():
    """Función principal."""
    app = InstagramAnalyzerApp(base_directory=Path.cwd())
    app.run()


if __name__ == "__main__":
    main()
