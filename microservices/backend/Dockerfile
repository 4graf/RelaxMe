FROM python:3.11-alpine

LABEL authors="Арсений"

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

ENV PYTHONPATH "${PYTHONPATH}:/backend"

COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend
CMD python main.py
