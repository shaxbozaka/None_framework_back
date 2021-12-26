
# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN echo "salom" > salom.txt
EXPOSE 3306
EXPOSE 8000
EXPOSE 8080
COPY . .
RUN ls -la
CMD ["python", "manage.py"]
