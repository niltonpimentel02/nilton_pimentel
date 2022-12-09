FROM python:3.10.0-slim

MAINTAINER Nilton Pimentel <contato@niltonpimentel.com.br>

COPY . /app
WORKDIR /app

RUN apt update -y && apt upgrade -y && apt autoremove -y

RUN python3 -m venv /opt/.venv --upgrade-deps

RUN /opt/.venv/bin/pip install pip install wheel && \
    /opt/.venv/bin/pip install pip --upgrade && \
    /opt/.venv/bin/pip install --no-cache-dir -r requirements-dev.txt

EXPOSE 8000
