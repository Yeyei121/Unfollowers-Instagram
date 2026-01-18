# Guía de Uso - Instagram Follower Analyzer

## 🚀 Inicio Rápido

### Paso 1: Instalación

```bash
# Navegar al directorio del proyecto
cd Unfollowers_Instagram

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 2: Obtener SessionID

1. Abre **Instagram** en tu navegador
2. Inicia sesión con tu cuenta
3. Presiona **F12** (abre DevTools)
4. Ve a la pestaña **Application** (Chrome) o **Storage** (Firefox)
5. En el menú izquierdo: **Cookies** → **https://www.instagram.com**
6. Busca `sessionid` y **copia su valor**

### Paso 3: Ejecutar

```bash
python main.py
```

## 📖 Tutorial Completo

### Primera vez usando la aplicación

```
=======================================================================
  📱 ANALIZADOR DE SEGUIDORES DE INSTAGRAM
=======================================================================

ℹ️  Aplicación para analizar quién te dejó de seguir en Instagram

🔐 MENÚ PRINCIPAL
   1. Crear sesión desde cookies del navegador
   2. Cargar sesión guardada
   3. Analizar seguidores
   4. Salir

Selecciona una opción: 1
```

**Opción 1: Crear sesión**

```
=======================================================================
  🔐 OBTENER SESSIONID DE INSTAGRAM
=======================================================================

📋 PASOS:
   1. Abre Instagram en tu navegador (con sesión activa)
   2. Presiona F12 para abrir DevTools
   3. Ve a: Application → Cookies → https://www.instagram.com
   4. Busca la cookie 'sessionid' y copia su valor

👤 Usuario de Instagram: tu_usuario
🔑 SessionID: [pega aquí el sessionid copiado]

🔐 Autenticando...
✓ Sesión válida para @tu_usuario
  • Seguidores: 1250
  • Seguidos: 890
✓ Sesión creada y guardada exitosamente
```

### Usos posteriores

Si ya creaste una sesión, puedes cargarla directamente:

```
🔐 MENÚ PRINCIPAL
   1. Crear sesión desde cookies del navegador
   2. Cargar sesión guardada
   3. Analizar seguidores
   4. Salir

Selecciona una opción: 2

👤 Usuario de la sesión guardada: tu_usuario

🔐 Cargando sesión...
✓ Sesión válida para @tu_usuario
  • Seguidores: 1250
  • Seguidos: 890
✓ Sesión cargada exitosamente
```

### Analizar seguidores

```
Selecciona una opción: 3

⚠️  El proceso puede tardar varios minutos...
ℹ️  Instagram limita la velocidad de las solicitudes

¿Deseas continuar? (S/n): s

📊 Analizando cuenta @tu_usuario...

📥 Obteniendo seguidores de @tu_usuario...
   Procesados 50 seguidores...
   Procesados 100 seguidores...
   ...
✓ Total de seguidores: 1250

📤 Obteniendo seguidos de @tu_usuario...
   Procesados 50 seguidos...
   Procesados 100 seguidos...
   ...
✓ Total de seguidos: 890

🔍 Analizando datos...

=======================================================================
📊 RESUMEN DEL ANÁLISIS
=======================================================================

📈 ESTADÍSTICAS:
   • Total de seguidores: 1250
   • Total de seguidos: 890
   • Seguidores mutuos: 780 (87.6%)
   • Te siguen pero no los sigues: 470
   • Los sigues pero no te siguen: 110 (12.4%)

⚠️  Hay 110 usuarios que no te siguen de vuelta

¿Deseas exportar los resultados? (S/n): s
```

### Exportar resultados

```
💾 ¿QUÉ DESEAS EXPORTAR?
   1. Exportar reporte completo (TXT)
   2. Exportar reporte completo (JSON)
   3. Exportar solo lista de unfollowers
   4. No exportar

Selecciona una opción: 1

💾 Reporte guardado en: instagram_analysis_20260115_143052.txt

✓ Análisis completado exitosamente!
```

## 📄 Formatos de Exportación

### 1. Reporte TXT

Archivo de texto legible con toda la información:

```
=======================================================================
📊 REPORTE DE ANÁLISIS DE SEGUIDORES
=======================================================================

Fecha: 2026-01-15 14:30:52

📈 ESTADÍSTICAS GENERALES:
   • Total de seguidores: 1250
   • Total de seguidos: 890
   • Seguidores mutuos: 780 (87.6%)
   • Te siguen pero no los sigues: 470
   • Los sigues pero no te siguen: 110 (12.4%)

⚠️  USUARIOS QUE NO TE SIGUEN DE VUELTA (110):
   1. @usuario1
   2. @usuario2
   3. @usuario3
   ...

👥 USUARIOS QUE TE SIGUEN Y NO SIGUES (470):
   (Lista muy larga, mostrando primeros 20)
   1. @usuario_A
   2. @usuario_B
   ...
```

### 2. Reporte JSON

Datos estructurados para procesamiento programático:

```json
{
  "followers": ["user1", "user2", ...],
  "following": ["user3", "user4", ...],
  "mutual_followers": ["user5", "user6", ...],
  "not_following_back": ["user7", "user8", ...],
  "not_followed_back": ["user9", "user10", ...],
  "statistics": {
    "total_followers": 1250,
    "total_following": 890,
    "mutual_followers": 780,
    "not_following_back": 110,
    "not_followed_back": 470,
    "mutual_percentage": 87.6,
    "unfollowers_percentage": 12.4
  },
  "export_date": "2026-01-15T14:30:52"
}
```

### 3. Lista de Unfollowers

Archivo simple con solo los usuarios que no te siguen:

```
Usuarios que no te siguen de vuelta (110)
Generado: 2026-01-15 14:30:52

@usuario1
@usuario2
@usuario3
@usuario4
...
```

## ⚠️ Solución de Problemas

### Error: "No se pudo autenticar"

**Causa**: SessionID inválido o expirado

**Solución**:
1. Vuelve a obtener el sessionid del navegador
2. Asegúrate de copiar el valor completo
3. Verifica que tu sesión de Instagram esté activa

### Error: "La sesión no es válida o ha expirado"

**Causa**: La sesión guardada ya no es válida

**Solución**:
1. Crea una nueva sesión (opción 1)
2. Las sesiones de Instagram expiran periódicamente

### El análisis tarda mucho tiempo

**Es normal**: Instagram limita las solicitudes para evitar abusos

**Consejos**:
- Sé paciente, puede tardar 5-10 minutos para cuentas grandes
- No interrumpas el proceso
- No ejecutes múltiples análisis seguidos

### Error: "Se requiere autenticación"

**Causa**: No has autenticado o la sesión expiró

**Solución**:
1. Selecciona opción 1 o 2 primero
2. Verifica que la autenticación fue exitosa
3. Luego ejecuta opción 3

## 💡 Consejos

1. **Guarda tu sessionid de forma segura**: No lo compartas con nadie

2. **Usa sesiones guardadas**: No necesitas obtener el sessionid cada vez

3. **Analiza periódicamente**: Ejecuta el análisis cada semana/mes para llevar un seguimiento

4. **Guarda los reportes**: Los reportes incluyen fecha, útil para comparar cambios

5. **No abuses**: Ejecuta el análisis con moderación para evitar bloqueos temporales

## 🔄 Comparar Análisis en el Tiempo

Puedes guardar reportes con diferentes fechas para ver cambios:

```bash
# Análisis actual
instagram_analysis_20260115_143052.txt

# Análisis del mes pasado
instagram_analysis_20251215_120030.txt

# Comparar manualmente para ver:
# - Quién te dejó de seguir desde el mes pasado
# - Quién te empezó a seguir
# - Cambios en estadísticas
```

## 📊 Interpretación de Resultados

### Seguidores Mutuos (Mutual Followers)
- Usuarios con los que hay seguimiento recíproco
- **Porcentaje alto** = Buena interacción
- **Porcentaje bajo** = Podrías estar siguiendo muchas cuentas inactivas

### No te siguen de vuelta (Unfollowers)
- Usuarios que sigues pero no te siguen
- **Número alto** = Considera dejar de seguir algunas cuentas
- Revisa si son cuentas importantes para ti

### Te siguen pero no los sigues
- Potenciales nuevos seguidores para interactuar
- Considera seguir de vuelta si te interesan

## 🎯 Mejores Prácticas

1. **Ejecuta el análisis regularmente** (semanal o mensual)
2. **Guarda los reportes** para llevar un histórico
3. **Revisa la lista de unfollowers** antes de dejar de seguir
4. **No dejes de seguir en masa** (puede verse como spam)
5. **Interactúa genuinamente** con tus seguidores

---

**¡Disfruta del análisis! 📱✨**
