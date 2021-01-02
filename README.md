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
- Configurado para correr en un entorno virtual de desarrollo o producción. El cambio de entorno de desarrollo o producción se hace colocando en el archivo manage.py dev o prod en DJANGO_SETTINGS_MODULE.
- Modificado el archivo setting.py a un directorio setting con los archivos:
	- base.py: settings comunes a desarrollo y producción
	- dev.py: settings para el entorno de desarrollo
	- prod.py: settings para el entorno de producción
- Se comenzo a trabajar para montar en un server mediante Docker, pero no se alcanzao a terminar de configurar


Ej. de desarrollo:

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.dev')


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

6) python manage.py makemigrations
7) python manage.py migrate
8) python manage.py createsuperuser

# Opcional, para rellenar la base de datos con valores precargados
python manage.py loaddata pre_data.json

# Para correr en desarrollo
python manage.py runserver

# Para configuar la aplicación en desarrollo
http://127.0.0.1:8000/admin

```

