# DeportesMundo — Instrucciones de Instalación y Despliegue

## Probar en tu PC primero

### 1. Instalar Python (si no lo tienes)
Descarga Python 3.11+ desde python.org e instálalo marcando "Add to PATH".

### 2. Instalar dependencias
Abre una terminal en la carpeta del proyecto y ejecuta:
```
pip install -r requirements.txt
```

### 3. Ejecutar la web localmente
```
python app.py
```
Abre el navegador en: http://localhost:5000

---

## Desplegar GRATIS en internet (Render.com)

### Paso 1 — Subir el código a GitHub
1. Crea una cuenta en github.com (si no tienes)
2. Crea un nuevo repositorio llamado `deportes-mundo`
3. Sube todos los archivos de esta carpeta al repositorio

### Paso 2 — Crear cuenta en Render.com
1. Ve a render.com y crea cuenta gratis
2. Haz clic en "New +" → "Web Service"
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio `deportes-mundo`

### Paso 3 — Configurar el servicio
- **Name**: deportes-mundo (o el nombre que quieras)
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free

Haz clic en "Create Web Service" y en 2-3 minutos tendrás tu URL:
`https://deportes-mundo.onrender.com`

---

## Lo que tiene la web

| Sección | Descripción |
|---|---|
| Inicio | Top noticias de todos los deportes |
| 🔥 Más Relevantes | Las noticias con más impacto del día |
| 💰 Monetizable | Noticias con alto potencial de contenido |
| /deporte/futbol | Todas las noticias de fútbol |
| /deporte/baloncesto | Todas las noticias de baloncesto |
| /deporte/tenis | Todas las noticias de tenis |
| /deporte/formula1 | Todas las noticias de Fórmula 1 |
| /jugador/[nombre] | Ficha Wikipedia + ideas de contenido |

---

## Agregar más deportes

En el archivo `feeds.py`, copia el bloque de cualquier deporte y modifica:
- `name`: nombre del deporte
- `emoji`: emoji representativo
- `color`: color en hexadecimal
- `feeds`: URLs de RSS en español para ese deporte
- `historicos` y `actuales`: lista de jugadores/deportistas

Luego en `app.py` ya se incluye automáticamente.

---

## Monetización con Google AdSense

Una vez que la web tenga tráfico:
1. Crea cuenta en Google AdSense
2. Agrega el código de AdSense en `templates/base.html` dentro del `<head>`
3. Los anuncios aparecerán automáticamente en la web

---

## Noticias que se actualizan
Las noticias se refrescan automáticamente cada 30 minutos desde las fuentes RSS.
No hay que hacer nada manual.