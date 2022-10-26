# pull official base image
FROM python:3.11.0-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./
RUN apt-get update && apt-get install -y python3-dev make
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
