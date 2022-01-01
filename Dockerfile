
# syntax=docker/dockerfile:1
FROM python:3.9
FROM shaxbozaka
FROM ubuntu
FROM mysql:latest
WORKDIR /
COPY requirements.txt requirements.txt
RUN apt install python3.9-pip
RUN pip install -r requirements.txt
RUN apt-get update
EXPOSE 3306
EXPOSE 8000
EXPOSE 8080
COPY . .
RUN docker-compose build
CMD ["python", "manage.py", "docker"]
