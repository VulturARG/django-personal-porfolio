# Personal Portfolio

## Framework: Django

## Description:
This application show a personal portfolio of a developer, where their work, their knowledge and skills can be exposed.

Have 3 fixed pages:
- **Welcome:** home or index page. Divided into a title and description, configurable by the administrator and saved in the database. Must be configured prior to use.
- **Portfolio:** Page where the different projects are shown with an image, a summary and has a link to a details page. The projects are configurable by the administrator and saved in the database.
- **Skill Set:** Page where the different skills or knowledge are displayed. The skill are configurable by the administrator and saved in the database.
  
In addition, extra pages can be created dynamically from the administration panel, which consist of a title and a description. They are saved in the database.

## Technical characteristics:
- Development environment using manage.py
- Production environment using manage-prod.py
- Changed the setting.py file to a setting directory with the files:
	- base.py: settings common to development and production
	- dev.py: settings for the development environment
	- prod.py: settings for the production environment

## Installation in development environment

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

### First time run in development environment
```bash
6) python manage.py makemigrations
7) python manage.py migrate
8) python manage.py createsuperuser

# Optional, to populate the database with preloaded values
python manage.py loaddata pre_data.json

# To run in development
python manage.py runserver

# To configure the application
http://127.0.0.1:8000/admin
```

## Installation and start up in production environment with Docker
```bash
1) Install Docker
2) Install Docker Composer

3) sudo git clone https://github.com/VulturARG/django-personal-porfolio.git
4) cd django-personal-porfolio
5) Create file .env (Formato abajo)
6) docker-compose up -d
7) docker-compose exec django_gunicorn python3 manage-prod.py migrate

# Optional, to populate the database with preloaded values
# If it does not run, skip to step 7) The data should be loaded manually from / admin BEFORE running the application so that no error
8) docker-compose exec django_gunicorn python3 manage-prod.py loaddata pre_data.json

9) docker-compose exec django_gunicorn python3 manage-prod.py createsuperuser
```

### To configure the application
```bash
http://xxx.xxx.xxx.xxx:8000/admin
```
### To examine inside the container.
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

To dump database to file:
```bash
python manage.py dumpdata projects --indent 2 > test.json
```

Source docker-compose producción
https://youtu.be/vJAfq6Ku4cI

github: (Fork)
https://github.com/VulturARG/django-docker-compose


Estudiar 
https://emilyemorehouse.com/017-debug-django-with-docker-vs-code/
