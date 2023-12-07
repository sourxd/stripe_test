FROM python:3.10.13-alpine3.17

ENV PYTHONUNBUFFERED 1

RUN mkdir /stripe
WORKDIR /stripe

COPY requirements.txt /stripe/requirements.txt

EXPOSE 8000

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN adduser --disabled-password admin

USER admin

ADD . /stripe
