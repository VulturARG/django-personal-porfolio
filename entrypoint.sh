#!/bin/sh

python3 manage-prod.py migrate
# python3 manage-prod.py collectstatic --no-input
python3 manage-prod.py loaddata ./portfolio/pre_data.json

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

