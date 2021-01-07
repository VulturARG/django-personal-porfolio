#!/bin/sh

python3 manage-prod.py migrate

# python3 manage-prod.py collectstatic --no-input
python3 manage-prod.py loaddata pre_data.json

## docker-compose exec web python manage.py createsuperuser
## docker-compose exec django_gunicorn bash 

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

