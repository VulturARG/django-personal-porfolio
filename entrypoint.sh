#!/bin/sh

<<<<<<< HEAD
# rm -rf static

# python3 manage-prod.py migrate --no-input
=======
# python3 manage-prod.py migrate
>>>>>>> bd26d0e4e132b5a4273dce28eb270cdf75b62b6d

# python3 manage-prod.py collectstatic --no-input

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

