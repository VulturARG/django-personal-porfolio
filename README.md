# Personal Portfolio

## Framework: Django

## Descripción:
Esta aplicación permite la publicación de un portafolio personal de un desarrollador, donde se pueden exponer sus trabajos y sus conocimientos y habilidades.

Consta de 3 páginas fijas:
- **Welcome:** Página de bienvenida (home o index) Dividido en un título y una descripción configurables por el administrador y guardados en la base de datos.
- **Portfolio:** Página donde se muestran los distintos proyectos con una imagen, un resumen y cuenta con un link a una página de detalles. Son configurables por el administrador y guardados en la base de datos.
- **Skill Set:** Página donde se muestran las diferentes habilidades o conocimientos. Son configurables por el administrador y guardados en la base de datos.
Además, se pueden crear paginas dinámicamente desde el panel de administración, las cuales constan de un título y una descripción. Se guardan en la base de datos.

Se agregó para esta entrega una página de ejemplo de uso de tecnología Ajax y JQurry UI

## Características técnicas:
- Entorno de desarrollo usando manage.py
- Entorno de producción usando manage-prod.py
- Cambiado el archivo setting.py a un directorio setting con los archivos:
	- base.py: settings comunes a desarrollo y producción
	- dev.py: settings para el entorno de desarrollo
	- prod.py: settings para el entorno de producción
- Se comenzo a trabajar para montar en un server mediante Docker, pero no se alcanzo a terminar de configurar

## Instalación
Cambiar dev o prod en DJANGO_SETTINGS_MODULE según lo indicado en el punto anterior

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

### Correr en entorno de producción
```bash
6) python manage-prod.py makemigrations
7) python manage-prod.py migrate
8) python manage-prod.py createsuperuser

# Opcional, para rellenar la base de datos con valores precargados
python manage-prod.py loaddata pre_data.json
```

### Para configuar la aplicación
```bash
http://xxx.xxx.xxx.xxx:8000/admin
```

Fuente docker-compose producción
https://youtu.be/vJAfq6Ku4cI

github: (Fork)
https://github.com/VulturARG/django-docker-compose

