FROM debian:buster-slim

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
            python3 \
            python3-pip \
            python3-dev \
<<<<<<< HEAD
            libpq-dev \
            tree
=======
            libpq-dev
>>>>>>> bd26d0e4e132b5a4273dce28eb270cdf75b62b6d

# RUN pip3 install --upgrade pip

RUN pip3 install --upgrade wheel==0.34.2 setuptools==49.6.0
<<<<<<< HEAD

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./portfolio /app

WORKDIR /app

RUN rm -rfv static
RUN python3 manage-prod.py migrate
RUN python3 manage-prod.py collectstatic --no-input
=======

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./portfolio /app

WORKDIR /app
>>>>>>> bd26d0e4e132b5a4273dce28eb270cdf75b62b6d

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

