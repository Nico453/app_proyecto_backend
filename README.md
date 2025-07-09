# Proyecto Django

Este repositorio contiene un proyecto web desarrollado con Django. Incluye una configuración base para crear APIs, manejar autenticación con JWT y documentación automática usando Swagger.

## 🚀 Tecnologías utilizadas

- Python 3.x
- Django 5.2.1
- Django REST Framework
- JWT (Autenticación con `djangorestframework_simplejwt`)
- PostgreSQL (con `psycopg2-binary`)
- Swagger (vía `drf-yasg`)
- Variables de entorno con `python-dotenv`
- CORS middleware

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Nico453/app_proyecto_backend.git
cd app_proyecto_backend
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requerimientos.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las variables necesarias, por ejemplo:

```
# Seguridad y entorno
SECRET_KEY=tu_clave_secreta
DEBUG=True
DEBUG_PROD=False

# Hosts permitidos (usa * solo para desarrollo local)
ALLOWED_HOSTS=localhost,127.0.0.1

# Configuración de la base de datos PostgreSQL
DATABASE_NAME=nombre_base_datos
DATABASE_USERNAME=usuario
DATABASE_PASSWORD=contraseña
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Configuración de correo para envío de emails (por ejemplo: recuperación de contraseña)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_o_token_app
DEFAULT_FROM_EMAIL=${EMAIL_HOST_USER}

```

### 5. Migraciones y servidor de desarrollo

```bash
python manage.py migrate
python manage.py runserver
```



## 🔐 Autenticación

Este proyecto usa JWT con `djangorestframework_simplejwt`. Puedes autenticarte enviando tu usuario y contraseña al endpoint:

```
POST http://127.0.0.1:8000/api/auth/login/
```

Obtendrás un `access` y `refresh token` para usar en llamadas protegidas.

## 📄 Documentación

La documentación Swagger está disponible en:

```
/swagger/
http://127.0.0.1:8000/docs/
o
http://127.0.0.1:8000/redocs/
```

## ✅ Requisitos (`requeriminetos.txt`)

```txt
asgiref==3.8.1
Django==5.2.1
django-cors-headers==4.7.0
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
drf-yasg==1.21.10
inflection==0.5.1
packaging==25.0
psycopg2-binary==2.9.10
PyJWT==2.9.0
python-dotenv==1.1.0
pytz==2025.2
PyYAML==6.0.2
sqlparse==0.5.3
tzdata==2025.2
uritemplate==4.2.0
```

