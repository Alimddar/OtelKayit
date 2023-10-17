FROM python:3.8.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /proje

COPY requirements.txt /proje/

RUN pip install -r requirements.txt

COPY . .