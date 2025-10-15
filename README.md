# Formulario de Contacto U La Salle

Una aplicación web moderna desarrollada con Flask para el formulario de contacto de la Universidad La Salle.

## 🚀 Características

- **Página principal** con información institucional
- **Formulario de contacto** funcional con validación
- **Base de datos SQLite** para almacenar mensajes
- **Diseño responsivo** y moderno
- **Interfaz intuitiva** con iconos y animaciones
- **Mensajes flash** para feedback del usuario

## 📋 Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación Local

### 1. Clonar o descargar el proyecto
```bash
# Si tienes git instalado
git clone <url-del-repositorio>
cd formulario_contacto_lasalle

# O simplemente descarga y extrae el archivo ZIP
```

### 2. Crear un entorno virtual (recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

### 5. Acceder a la aplicación
Abre tu navegador y ve a: `http://localhost:5000`

## 🌐 Despliegue en la Nube (Gratuito)

### Opción 1: Heroku (Recomendado)

1. **Crear cuenta en Heroku**: https://heroku.com
2. **Instalar Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
3. **Crear archivo Procfile**:
```
web: gunicorn app:app
```
4. **Modificar app.py** para producción:
```python
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```
5. **Comandos para desplegar**:
```bash
heroku login
heroku create tu-app-lasalle
git add .
git commit -m "Initial commit"
git push heroku main
```

### Opción 2: Railway

1. **Crear cuenta en Railway**: https://railway.app
2. **Conectar con GitHub** y seleccionar tu repositorio
3. **Railway detectará automáticamente** que es una aplicación Flask
4. **Configurar variables de entorno** si es necesario
5. **Desplegar** con un clic

### Opción 3: Render

1. **Crear cuenta en Render**: https://render.com
2. **Conectar repositorio** desde GitHub
3. **Configurar**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. **Desplegar**

### Opción 4: PythonAnywhere

1. **Crear cuenta gratuita**: https://pythonanywhere.com
2. **Crear nueva aplicación web**
3. **Subir archivos** via consola o interfaz web
4. **Configurar WSGI** para Flask
5. **Configurar dominio** personalizado

## 📁 Estructura del Proyecto

```
formulario_contacto_lasalle/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias de Python
├── README.md             # Este archivo
├── contactos.db          # Base de datos SQLite (se crea automáticamente)
├── static/
│   └── style.css         # Estilos CSS
└── templates/
    ├── index.html        # Página principal
    └── contacto.html     # Formulario de contacto
```

## 🗄️ Base de Datos

La aplicación utiliza SQLite para almacenar los mensajes de contacto. La base de datos se crea automáticamente al ejecutar la aplicación por primera vez.

### Estructura de la tabla `contactos`:
- `id`: Identificador único (auto-incremento)
- `nombre`: Nombre completo del usuario
- `email`: Correo electrónico
- `telefono`: Número de teléfono (opcional)
- `mensaje`: Mensaje del usuario
- `fecha`: Fecha y hora del envío (automática)

## 🔧 Configuración Adicional

### Variables de Entorno
Para producción, configura estas variables:
```bash
export FLASK_ENV=production
export SECRET_KEY=tu_clave_secreta_muy_segura
```

### Personalización
- **Colores**: Modifica las variables CSS en `static/style.css`
- **Contenido**: Edita los textos en `templates/index.html` y `templates/contacto.html`
- **Configuración**: Ajusta la configuración en `app.py`

## 🧪 Pruebas Locales

### Probar el formulario:
1. Ve a `http://localhost:5000/contacto`
2. Completa el formulario
3. Envía el mensaje
4. Verifica que aparezca el mensaje de confirmación

### Ver mensajes almacenados:
1. Ve a `http://localhost:5000/admin`
2. Revisa los mensajes guardados en la base de datos

## 🚀 Comandos Útiles

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en modo desarrollo
python app.py

# Ejecutar en modo producción
gunicorn app:app

# Ver logs en Heroku
heroku logs --tail

# Abrir aplicación en Heroku
heroku open
```

## 📞 Soporte

Si tienes problemas con el despliegue:

1. **Verifica los logs** de la plataforma de despliegue
2. **Revisa que todas las dependencias** estén instaladas
3. **Confirma que el puerto** esté configurado correctamente
4. **Verifica las variables de entorno** si las usas

## 🎯 Próximos Pasos

- [ ] Agregar autenticación para el panel de administración
- [ ] Implementar envío de emails automáticos
- [ ] Agregar más validaciones al formulario
- [ ] Implementar captcha para prevenir spam
- [ ] Agregar más campos al formulario (asunto, tipo de consulta, etc.)

## 📄 Licencia

Este proyecto es para fines educativos de la Universidad La Salle.

---

**Desarrollado con ❤️ para U La Salle**
