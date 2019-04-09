FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /food_crm

WORKDIR /food_crm

ADD . /food_crm/


RUN pip install -r requirements.txt