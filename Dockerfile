FROM python:3.8

RUN mkdir /code
WORKDIR /code

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ADD . /code/
