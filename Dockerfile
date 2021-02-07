FROM debian:buster-slim

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
            python3 \
            python3-pip \
            python3-dev \
            libpq-dev \
            tree

# RUN pip3 install --upgrade pip

RUN pip3 install --upgrade wheel==0.34.2 setuptools==49.6.0

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./portfolio /app

WORKDIR /app

RUN python3 manage-prod.py collectstatic --no-input

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

