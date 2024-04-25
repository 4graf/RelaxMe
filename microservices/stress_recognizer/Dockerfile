FROM python:3.11-alpine

LABEL authors="Арсений"

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED 1

WORKDIR /stress_recognizer

ENV PYTHONPATH "${PYTHONPATH}:/stress_recognizer"

COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install --no-cache-dir torch torchvision torchaudio -f --index-url https://download.pytorch.org/whl/cpu

COPY . /stress_recognizer
CMD python main.py
