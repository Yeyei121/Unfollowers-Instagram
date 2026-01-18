# Analizador de Seguidores de Instagram 

Aplicación profesional para analizar tus seguidores de Instagram y descubrir quién te dejó de seguir.

## Características

- ✅ Análisis completo de seguidores y seguidos
- ✅ Identificación de usuarios que no te siguen de vuelta
- ✅ Estadísticas detalladas con porcentajes
- ✅ Exportación de reportes en múltiples formatos (TXT, JSON)
- ✅ Gestión de sesiones persistentes
- ✅ Autenticación segura mediante cookies del navegador
- ✅ Interfaz de consola intuitiva y amigable

## 🏗️ Arquitectura

Este proyecto ha sido desarrollado siguiendo **buenas prácticas de programación**:

### Patrones de Diseño

- **Repository Pattern**: `InstagramRepository` encapsula el acceso a datos
- **Facade Pattern**: `InstagramAnalyzerApp` simplifica la interacción con todos los módulos
- **Strategy Pattern**: Diferentes estrategias de autenticación (cookies, sesión guardada)
- **Factory Method**: Creación de diferentes tipos de exportadores

### Estructura Modular

```
src/
├── auth/               # Autenticación y gestión de sesiones
│   ├── interfaces.py
│   ├── session_manager.py
│   └── cookie_provider.py
├── data/               # Acceso a datos de Instagram
│   ├── interfaces.py
│   └── instagram_repository.py
├── analysis/           # Análisis de seguidores
│   ├── models.py
│   ├── follower_analyzer.py
│   └── statistics_calculator.py
├── utils/              # Utilidades (archivos, reportes)
│   ├── file_manager.py
│   └── report_exporter.py
├── ui/                 # Interfaz de usuario
│   ├── console_printer.py
│   ├── input_validator.py
│   └── menu_manager.py
└── app.py              # Aplicación principal
```

## Requisitos

- Python 3.8 o superior
- Cuenta de Instagram
- Navegador web (Chrome, Firefox, Edge, etc.)

## Instalación

1. **Clonar o descargar el proyecto**

```bash
cd Unfollowers_Instagram
```

2. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

## Uso

### 1. Ejecutar la aplicación

```bash
python main.py
```

### 2. Obtener SessionID de Instagram

Para autenticarte, necesitas obtener tu `sessionid` de Instagram:

1. Abre Instagram en tu navegador (con sesión iniciada)
2. Presiona **F12** para abrir DevTools
3. Ve a: **Application** → **Cookies** → **https://www.instagram.com**
4. Busca la cookie `sessionid` y copia su valor

### 3. Crear sesión

En el menú principal, selecciona la opción 1:
- Ingresa tu nombre de usuario de Instagram
- Pega el `sessionid` que copiaste
- La sesión se guardará para usos futuros

### 4. Analizar seguidores

Una vez autenticado, selecciona la opción 3 para:
- Obtener tu lista de seguidores
- Obtener tu lista de seguidos
- Analizar quién no te sigue de vuelta
- Ver estadísticas detalladas

### 5. Exportar resultados

Puedes exportar los resultados en diferentes formatos:
- **Reporte TXT**: Reporte completo legible
- **Reporte JSON**: Datos estructurados para procesamiento
- **Lista de unfollowers**: Solo usuarios que no te siguen

## Ejemplo de Salida

```
=======================================================================
RESUMEN DEL ANÁLISIS
=======================================================================

📈 ESTADÍSTICAS:
   • Total de seguidores: 1250
   • Total de seguidos: 890
   • Seguidores mutuos: 780 (87.6%)
   • Te siguen pero no los sigues: 470
   • Los sigues pero no te siguen: 110 (12.4%)

⚠️  Hay 110 usuarios que no te siguen de vuelta
```

## 🔒 Seguridad y Privacidad

- ✅ **No almacenamos contraseñas**: Solo usamos cookies de sesión
- ✅ **Sesiones locales**: Toda la información se guarda en tu computadora
- ✅ **Sin servidores externos**: La aplicación funciona 100% offline
- ✅ **Código abierto**: Puedes revisar todo el código fuente

## ⚠️ Notas Importantes

- Instagram limita la velocidad de las solicitudes, el análisis puede tardar varios minutos
- La sesión puede expirar después de cierto tiempo
- No abuses de las solicitudes para evitar que Instagram bloquee temporalmente tu cuenta
- Usa la aplicación de manera responsable

## Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación
- **Instaloader**: Biblioteca para interactuar con Instagram
- **Type Hints**: Para mejor legibilidad y mantenibilidad
- **Dataclasses**: Para modelos de datos inmutables
- **ABC (Abstract Base Classes)**: Para definir interfaces

## 📧 Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio.

---

**¡Disfruta analizando tus seguidores de Instagram! **
