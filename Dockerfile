
# syntax=docker/dockerfile:1
FROM python:3.9

WORKDIR /
COPY requirements.txt requirements.txt
RUN set -xe \
    && apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 3306
EXPOSE 8000
EXPOSE 8080
COPY . .

CMD ["python", "manage.py", "docker"]
