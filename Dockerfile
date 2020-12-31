FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

RUN python portfolio/manage.py makemigrations
RUN python portfolio/manage.py migrate
RUN python portfolio/manage.py loaddata portfolio/pre_data.json

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "portfolio", "portfolio.wsgi:application"]
