# Pull base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

RUN useradd django

RUN mkdir -p /opt/django \
    && chown django /opt/django \
    && chmod -R 777 /opt/django
VOLUME ["/opt/django"]

WORKDIR /opt/django


COPY requirements.txt /opt/django/
COPY ./config_docker/gunicorn/gunicorn-cfg.py /opt/django/

COPY portfolio /opt/django/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations --settings=portfolio.settings.prod
RUN python manage.py migrate --settings=portfolio.settings.prod
RUN python manage.py loaddata pre_data.json --settings=portfolio.settings.prod


EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "portfolio.wsgi"]
