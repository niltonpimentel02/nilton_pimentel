FROM python:3.10.0-slim

MAINTAINER Nilton Pimentel <contato@niltonpimentel.com.br>

RUN apt-get update -y
RUN pip3 install --upgrade pip

ADD . /opt

RUN pip install -r /opt/requirements.txt -U

ENV PYTHONPATH $PYTHONPATH:/opt
WORKDIR /opt

EXPOSE 8900
