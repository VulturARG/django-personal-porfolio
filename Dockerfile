FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . /opt

WORKDIR /opt

RUN pip install -r requirements.txt

RUN python portfolio/manage-prod.py makemigrations
RUN python portfolio/manage-prod.py migrate
RUN python portfolio/manage-prod.py loaddata portfolio/pre_data.json

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "portfolio", "portfolio.wsgi:application"]


