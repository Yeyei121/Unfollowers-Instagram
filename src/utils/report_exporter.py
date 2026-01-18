"""
Exportadores de reportes.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from ..analysis.models import FollowerAnalysisResult
from .file_manager import FileManager


class ReportExporter(ABC):
    """
    Interfaz para exportadores de reportes.
    Siguiendo Open/Closed Principle: abierto para extensión, cerrado para modificación.
    """
    
    @abstractmethod
    def export(self, result: FollowerAnalysisResult, filename: Optional[str] = None) -> bool:
        """
        Exporta el resultado del análisis.
        
        Args:
            result: Resultado del análisis.
            filename: Nombre del archivo (opcional).
            
        Returns:
            bool: True si la exportación fue exitosa.
        """
        pass


class TextReportExporter(ReportExporter):
    """
    Exportador de reportes en formato texto.
    """
    
    def __init__(self, file_manager: FileManager):
        """
        Inicializa el exportador.
        
        Args:
            file_manager: Gestor de archivos.
        """
        self._file_manager = file_manager
    
    def export(self, result: FollowerAnalysisResult, filename: Optional[str] = None) -> bool:
        """
        Exporta el resultado a un archivo de texto.
        
        Args:
            result: Resultado del análisis.
            filename: Nombre del archivo.
            
        Returns:
            bool: True si se exportó exitosamente.
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"instagram_analysis_{timestamp}.txt"
        
        content = self._generate_text_report(result)
        success = self._file_manager.write_text_file(filename, content)
        
        if success:
            print(f"💾 Reporte guardado en: {filename}")
        
        return success
    
    def _generate_text_report(self, result: FollowerAnalysisResult) -> str:
        """
        Genera el contenido del reporte en texto.
        
        Args:
            result: Resultado del análisis.
            
        Returns:
            str: Contenido del reporte.
        """
        lines = []
        stats = result.statistics
        
        lines.append("=" * 70)
        lines.append("📊 REPORTE DE ANÁLISIS DE SEGUIDORES")
        lines.append("=" * 70)
        lines.append(f"\nFecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        lines.append("\n\n📈 ESTADÍSTICAS GENERALES:")
        lines.append(f"   • Total de seguidores: {stats.total_followers}")
        lines.append(f"   • Total de seguidos: {stats.total_following}")
        lines.append(f"   • Seguidores mutuos: {stats.mutual_followers} ({stats.mutual_percentage:.1f}%)")
        lines.append(f"   • Te siguen pero no los sigues: {stats.not_followed_back}")
        lines.append(f"   • Los sigues pero no te siguen: {stats.not_following_back} ({stats.unfollowers_percentage:.1f}%)")
        
        # Lista de usuarios que no te siguen de vuelta
        not_following_back = sorted(result.not_following_back)
        if not_following_back:
            lines.append(f"\n\n⚠️  USUARIOS QUE NO TE SIGUEN DE VUELTA ({len(not_following_back)}):")
            for i, user in enumerate(not_following_back, 1):
                lines.append(f"   {i}. @{user}")
        else:
            lines.append("\n\n✓ Todos los usuarios que sigues te siguen de vuelta")
        
        # Lista de usuarios que te siguen pero no sigues
        not_followed_back = sorted(result.not_followed_back)
        if not_followed_back:
            lines.append(f"\n\n👥 USUARIOS QUE TE SIGUEN Y NO SIGUES ({len(not_followed_back)}):")
            if len(not_followed_back) <= 20:
                for i, user in enumerate(not_followed_back, 1):
                    lines.append(f"   {i}. @{user}")
            else:
                lines.append("   (Lista muy larga, mostrando primeros 20)")
                for i, user in enumerate(not_followed_back[:20], 1):
                    lines.append(f"   {i}. @{user}")
        
        lines.append("\n" + "=" * 70)
        
        return '\n'.join(lines)


class JSONReportExporter(ReportExporter):
    """
    Exportador de reportes en formato JSON.
    """
    
    def __init__(self, file_manager: FileManager):
        """
        Inicializa el exportador.
        
        Args:
            file_manager: Gestor de archivos.
        """
        self._file_manager = file_manager
    
    def export(self, result: FollowerAnalysisResult, filename: Optional[str] = None) -> bool:
        """
        Exporta el resultado a un archivo JSON.
        
        Args:
            result: Resultado del análisis.
            filename: Nombre del archivo.
            
        Returns:
            bool: True si se exportó exitosamente.
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"instagram_analysis_{timestamp}.json"
        
        data = result.to_dict()
        data['export_date'] = datetime.now().isoformat()
        
        success = self._file_manager.write_json_file(filename, data)
        
        if success:
            print(f"💾 Reporte JSON guardado en: {filename}")
        
        return success


class UnfollowersListExporter:
    """
    Exportador especializado para lista de unfollowers.
    """
    
    def __init__(self, file_manager: FileManager):
        """
        Inicializa el exportador.
        
        Args:
            file_manager: Gestor de archivos.
        """
        self._file_manager = file_manager
    
    def export(self, unfollowers: set, filename: str = "unfollowers.txt") -> bool:
        """
        Exporta la lista de unfollowers a un archivo.
        
        Args:
            unfollowers: Conjunto de usuarios que no te siguen.
            filename: Nombre del archivo.
            
        Returns:
            bool: True si se exportó exitosamente.
        """
        unfollowers_sorted = sorted(unfollowers)
        
        lines = [
            f"Usuarios que no te siguen de vuelta ({len(unfollowers_sorted)})",
            f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
        ]
        
        for user in unfollowers_sorted:
            lines.append(f"@{user}")
        
        content = '\n'.join(lines)
        success = self._file_manager.write_text_file(filename, content)
        
        if success:
            print(f"✓ Lista guardada en: {filename}")
        
        return success
