#!/bin/sh

# python3 manage-prod.py migrate

# python3 manage-prod.py collectstatic --no-input

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

