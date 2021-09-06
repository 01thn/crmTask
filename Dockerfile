FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install psycopg2
RUN apt-get update && apt-get install
RUN pip install -r requirements.txt
COPY . /app/