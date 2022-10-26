# pull official base image
FROM ubuntu:22.04

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./
RUN apt-get update && apt-get install -y python3-dev make python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
