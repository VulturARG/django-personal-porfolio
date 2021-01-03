FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

COPY /portfolio /opt/portfolio
COPY /config /opt/portfolio/config
COPY requirements.txt /opt/portfolio/requirements.txt

WORKDIR /opt/portfolio

RUN pip install -r requirements.txt

RUN python manage-prod.py makemigrations
RUN python manage-prod.py migrate
RUN python manage-prod.py loaddata pre_data.json

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "portfolio", "portfolio.wsgi:application"]

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
