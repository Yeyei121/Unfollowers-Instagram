# Estructura del Proyecto

```
Unfollowers_Instagram/
│
├── 📁 config/                          # Configuración
│   └── config.yaml                     # Archivo de configuración
│
├── 📁 src/                             # Código fuente principal
│   ├── __init__.py                     # Inicialización del paquete
│   ├── app.py                          # Aplicación principal (Facade)
│   │
│   ├── 📁 auth/                        # Módulo de autenticación
│   │   ├── __init__.py
│   │   ├── interfaces.py               # IAuthenticationProvider, ISessionManager
│   │   ├── session_manager.py          # InstaloaderSessionManager
│   │   └── cookie_provider.py          # CookieAuthProvider, SavedSessionAuthProvider
│   │
│   ├── 📁 data/                        # Módulo de acceso a datos
│   │   ├── __init__.py
│   │   ├── interfaces.py               # IInstagramRepository
│   │   └── instagram_repository.py     # InstagramRepository
│   │
│   ├── 📁 analysis/                    # Módulo de análisis
│   │   ├── __init__.py
│   │   ├── models.py                   # FollowerStatistics, FollowerAnalysisResult
│   │   ├── follower_analyzer.py        # FollowerAnalyzer
│   │   └── statistics_calculator.py    # StatisticsCalculator
│   │
│   ├── 📁 utils/                       # Módulo de utilidades
│   │   ├── __init__.py
│   │   ├── file_manager.py             # FileManager
│   │   └── report_exporter.py          # ReportExporter, TextReportExporter, etc.
│   │
│   └── 📁 ui/                          # Módulo de interfaz de usuario
│       ├── __init__.py
│       ├── console_printer.py          # ConsolePrinter
│       ├── input_validator.py          # InputValidator
│       └── menu_manager.py             # MenuManager, MenuItem
│
├── 📄 main.py                          # Punto de entrada de la aplicación
│
├── 📄 requirements.txt                 # Dependencias del proyecto
├── 📄 .gitignore                       # Archivos ignorados por Git
│
├── 📄 README.md                        # Documentación principal
├── 📄 ARCHITECTURE.md                  # Documentación de arquitectura
├── 📄 USAGE_GUIDE.md                   # Guía de uso detallada
├── 📄 COMPARISON.md                    # Comparación código viejo vs nuevo
│
└── 📄 Archivos originales (backup)     # Código original preservado
    ├── exportar_cookies_manual.py
    ├── follower_comparison.py
    ├── instagram_data.py
    └── main_instagram_instaloader.py
```

## 📦 Descripción de Módulos

### 🔐 auth/ - Autenticación
**Responsabilidad**: Gestionar autenticación y sesiones de Instagram

- **interfaces.py**: Define contratos (`IAuthenticationProvider`, `ISessionManager`)
- **session_manager.py**: Gestiona persistencia de sesiones
- **cookie_provider.py**: Proveedores de autenticación (cookies, sesión guardada)

**Principios aplicados**: 
- Dependency Inversion (interfaces)
- Single Responsibility (cada clase una función)
- Open/Closed (extensible vía herencia)

---

### 💾 data/ - Acceso a Datos
**Responsabilidad**: Obtener información de Instagram

- **interfaces.py**: Define contrato `IInstagramRepository`
- **instagram_repository.py**: Implementación usando Instaloader

**Patrones aplicados**:
- Repository Pattern
- Dependency Injection

---

### 📊 analysis/ - Análisis de Datos
**Responsabilidad**: Analizar relaciones de seguidores

- **models.py**: Modelos de datos (`FollowerStatistics`, `FollowerAnalysisResult`)
- **follower_analyzer.py**: Lógica de análisis
- **statistics_calculator.py**: Cálculo de estadísticas

**Principios aplicados**:
- Single Responsibility
- Data Classes (inmutabilidad)
- Separation of Concerns

---

### 🛠️ utils/ - Utilidades
**Responsabilidad**: Servicios auxiliares (archivos, exportación)

- **file_manager.py**: Operaciones de archivos (lectura/escritura)
- **report_exporter.py**: Exportación de reportes en múltiples formatos

**Patrones aplicados**:
- Strategy Pattern (diferentes exportadores)
- Template Method

---

### 🖥️ ui/ - Interfaz de Usuario
**Responsabilidad**: Interacción con el usuario

- **console_printer.py**: Formateo y presentación de mensajes
- **input_validator.py**: Validación de entradas del usuario
- **menu_manager.py**: Gestión de menús interactivos

**Principios aplicados**:
- Single Responsibility
- Separation of Concerns (UI separada de lógica)

---

### 🎭 app.py - Aplicación Principal
**Responsabilidad**: Coordinar todos los módulos

- Implementa patrón **Facade**
- Gestiona **Dependency Injection**
- Orquesta flujo de la aplicación

---

## 📈 Flujo de Dependencias

```
main.py
  ↓
app.py (Facade)
  ↓
┌─────────────┬──────────────┬─────────────┬──────────────┐
│             │              │             │              │
auth/      data/        analysis/     utils/          ui/
  ↓           ↓              ↓             ↓              ↓
Interfaces  Repo         Analyzer     Exporters     Printers
  ↓           ↓              ↓             ↓              ↓
Providers   Instagram    Models       FileManager  Validators
            API
```

## 🔗 Relaciones entre Módulos

### Inyección de Dependencias

```python
# Creación en app.py
session_manager = InstaloaderSessionManager()
auth_provider = CookieAuthProvider(session_manager, ...)
repository = InstagramRepository(auth_provider)
analyzer = FollowerAnalyzer(followers, following)
exporter = TextReportExporter(file_manager)
```

### Acoplamiento

- **Bajo acoplamiento**: Módulos se comunican via interfaces
- **Alta cohesión**: Cada módulo tiene responsabilidad clara
- **Fácil testing**: Se pueden inyectar mocks

---

## 📝 Archivos de Documentación

### README.md
- Descripción general del proyecto
- Características principales
- Instrucciones de instalación
- Uso básico
- Arquitectura general

### ARCHITECTURE.md
- Principios SOLID en detalle
- Patrones de diseño utilizados
- Explicación de cada módulo
- Diagramas de arquitectura
- Extensibilidad futura

### USAGE_GUIDE.md
- Tutorial paso a paso
- Ejemplos de uso
- Formatos de exportación
- Solución de problemas
- Mejores prácticas

### COMPARISON.md
- Comparación código original vs refactorizado
- Transformaciones principales
- Métricas de mejora
- Ejemplos específicos

---

## 🎯 Principios de Organización

1. **Modularidad**: Cada carpeta es un módulo independiente
2. **Separación de responsabilidades**: Cada archivo tiene un propósito claro
3. **Jerarquía lógica**: Estructura refleja la arquitectura
4. **Navegabilidad**: Fácil encontrar cualquier funcionalidad
5. **Escalabilidad**: Fácil agregar nuevos módulos

---

## 🔍 Encontrar Funcionalidad

### "¿Dónde está...?"

- **Autenticación**: `src/auth/`
- **Obtener datos de Instagram**: `src/data/`
- **Analizar seguidores**: `src/analysis/`
- **Guardar reportes**: `src/utils/report_exporter.py`
- **Menús y UI**: `src/ui/`
- **Punto de entrada**: `main.py`
- **Configuración**: `config/config.yaml`

---

## 🚀 Agregar Nueva Funcionalidad

### Nuevo exportador
1. Crear clase en `src/utils/report_exporter.py`
2. Heredar de `ReportExporter`
3. Implementar método `export()`
4. Registrar en `src/utils/__init__.py`

### Nueva fuente de datos
1. Crear implementación en `src/data/`
2. Implementar `IInstagramRepository`
3. Inyectar en `app.py`

### Nuevo tipo de análisis
1. Crear clase en `src/analysis/`
2. Seguir patrón de `FollowerAnalyzer`
3. Usar en `app.py`

---

