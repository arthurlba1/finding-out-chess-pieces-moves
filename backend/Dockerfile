FROM python:3.9.10-slim-buster

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /backend/
RUN pip install --upgrade pip
RUN pip install -r /backend/requirements.txt

COPY . /backend
WORKDIR /backend

VOLUME /backend/data
