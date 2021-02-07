#!/bin/sh

rm -rf static

python3 manage-prod.py migrate --no-input

python3 manage-prod.py collectstatic --no-input

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

