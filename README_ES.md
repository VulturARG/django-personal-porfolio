# Personal Portfolio

## Framework: Django

## Descripción:
Esta aplicación permite la publicación de un portafolio personal de un desarrollador, donde se pueden exponer sus trabajos y sus conocimientos y habilidades.

Consta de 3 páginas fijas:
- **Welcome:** Página de bienvenida (home o index) Dividido en un título y una descripción configurables por el administrador y guardados en la base de datos.
- **Portfolio:** Página donde se muestran los distintos proyectos con una imagen, un resumen y cuenta con un link a una página de detalles. Son configurables por el administrador y guardados en la base de datos.
- **Skill Set:** Página donde se muestran las diferentes habilidades o conocimientos. Son configurables por el administrador y guardados en la base de datos.
Además, se pueden crear paginas dinámicamente desde el panel de administración, las cuales constan de un título y una descripción. Se guardan en la base de datos.

## Características técnicas:
- Entorno de desarrollo usando manage.py
- Entorno de producción usando manage-prod.py
- Cambiado el archivo setting.py a un directorio setting con los archivos:
	- base.py: settings comunes a desarrollo y producción
	- dev.py: settings para el entorno de desarrollo
	- prod.py: settings para el entorno de producción

## Instalación en entorno de desarrollo

```bash
1) git clone https://github.com/VulturARG/django-personal-porfolio.git
2) cd django-personal-porfolio

# Virtualenv instalación (Linux)
3) virtualenv env
4) source env/bin/activate

# Virtualenv instalación (Windows)
3) virtualenv env
4) .\env\Scripts\activate

5) pip3 install -r requirements.txt
```

### Correr en entorno de desarrollo
```bash
6) python manage.py makemigrations
7) python manage.py migrate
8) python manage.py createsuperuser

# Opcional, para rellenar la base de datos con valores precargados
python manage.py loaddata pre_data.json

# Para correr en desarrollo
python manage.py runserver

# Para configuar la aplicación
http://127.0.0.1:8000/admin
```

## Instalación y puesta en marcha en entorno de producción con Docker
```bash
1) Instalar Docker
2) Instalar Docker Composer

3) sudo git clone https://github.com/VulturARG/django-personal-porfolio.git
4) cd django-personal-porfolio
5) Crear archivo .env (Formato abajo)
6) docker-compose up -d
7) docker-compose exec django_gunicorn python3 manage-prod.py migrate

# Opcional, para rellenar la base de datos con valores precargados
# Si no se ejecuta, saltar al paso 7) Los datos deberan cargarse manualmente desde /admin ANTES de correr la aplicación para que no de error
8) docker-compose exec django_gunicorn python3 manage-prod.py loaddata pre_data.json

9) docker-compose exec django_gunicorn python3 manage-prod.py createsuperuser
```

### Para configuar la aplicación
```bash
http://xxx.xxx.xxx.xxx:8000/admin
```
### Para examinar dentro del contenedor.
```bash
docker-compose exec django_gunicorn bash
```

```bash
## do not put this file under version control!
SECRET_KEY = 'S3cr3t_K3y'
##DEBUG=False
SERVER='XXX.XXX.XXX.XXX'

# database access credentials
ENGINE=django.db.backends.postgresql
DB_NAME=some_mame
POSTGRES_USER=user_postgres
POSTGRES_PASSWORD=password_postgres
DB_HOST=db
DB_PORT=5432
APP_PORT=8000
#superuser details
DJANGO_SU_NAME=admin
DJANGO_SU_EMAIL=admin12@admin.com
DJANGO_SU_PASSWORD=mypass123
```

Fuente docker-compose producción
https://youtu.be/vJAfq6Ku4cI

github: (Fork)
https://github.com/VulturARG/django-docker-compose

