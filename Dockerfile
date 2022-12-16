FROM ubuntu:20.04

RUN apt update \
    && apt install -y python3-dev wget

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app