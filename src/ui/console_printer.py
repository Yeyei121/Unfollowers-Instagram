"""
Impresora de consola.
"""

from typing import List
from ..analysis.models import FollowerAnalysisResult


class ConsolePrinter:
    """
    Impresora de mensajes en consola.
    Siguiendo Single Responsibility Principle: solo formatea y muestra información.
    """
    
    @staticmethod
    def print_header(title: str, width: int = 70):
        """
        Imprime un encabezado.
        
        Args:
            title: Título del encabezado.
            width: Ancho del encabezado.
        """
        print("\n" + "=" * width)
        print(f"  {title}")
        print("=" * width + "\n")
    
    @staticmethod
    def print_section(title: str):
        """
        Imprime un título de sección.
        
        Args:
            title: Título de la sección.
        """
        print(f"\n{title}")
    
    @staticmethod
    def print_success(message: str):
        """
        Imprime un mensaje de éxito.
        
        Args:
            message: Mensaje a imprimir.
        """
        print(f"✓ {message}")
    
    @staticmethod
    def print_error(message: str):
        """
        Imprime un mensaje de error.
        
        Args:
            message: Mensaje a imprimir.
        """
        print(f"✗ {message}")
    
    @staticmethod
    def print_warning(message: str):
        """
        Imprime un mensaje de advertencia.
        
        Args:
            message: Mensaje a imprimir.
        """
        print(f"⚠️  {message}")
    
    @staticmethod
    def print_info(message: str):
        """
        Imprime un mensaje informativo.
        
        Args:
            message: Mensaje a imprimir.
        """
        print(f"ℹ️  {message}")
    
    @staticmethod
    def print_options(options: List[str]):
        """
        Imprime una lista de opciones.
        
        Args:
            options: Lista de opciones.
        """
        for i, option in enumerate(options, 1):
            print(f"   {i}. {option}")
    
    @staticmethod
    def print_analysis_summary(result: FollowerAnalysisResult):
        """
        Imprime un resumen del análisis.
        
        Args:
            result: Resultado del análisis.
        """
        stats = result.statistics
        
        ConsolePrinter.print_header("📊 RESUMEN DEL ANÁLISIS")
        
        print("📈 ESTADÍSTICAS:")
        print(f"   • Total de seguidores: {stats.total_followers}")
        print(f"   • Total de seguidos: {stats.total_following}")
        print(f"   • Seguidores mutuos: {stats.mutual_followers} ({stats.mutual_percentage:.1f}%)")
        print(f"   • Te siguen pero no los sigues: {stats.not_followed_back}")
        print(f"   • Los sigues pero no te siguen: {stats.not_following_back} ({stats.unfollowers_percentage:.1f}%)")
        
        if stats.not_following_back > 0:
            print(f"\n⚠️  Hay {stats.not_following_back} usuarios que no te siguen de vuelta")
        else:
            print("\n✓ Todos los usuarios que sigues te siguen de vuelta")
    
    @staticmethod
    def print_cookie_instructions():
        """Imprime instrucciones para obtener cookies."""
        ConsolePrinter.print_header("🔐 OBTENER SESSIONID DE INSTAGRAM")
        
        print("📋 PASOS:")
        print("   1. Abre Instagram en tu navegador (con sesión activa)")
        print("   2. Presiona F12 para abrir DevTools")
        print("   3. Ve a: Application → Cookies → https://www.instagram.com")
        print("   4. Busca la cookie 'sessionid' y copia su valor")
        print("")
    
    @staticmethod
    def print_verification_message(username: str, followers_count: int, following_count: int):
        """
        Imprime mensaje de verificación de sesión.
        
        Args:
            username: Nombre de usuario.
            followers_count: Cantidad de seguidores.
            following_count: Cantidad de seguidos.
        """
        ConsolePrinter.print_success(f"Sesión válida para @{username}")
        print(f"  • Seguidores: {followers_count}")
        print(f"  • Seguidos: {following_count}")
