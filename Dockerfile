# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm

COPY requirements.txt requirements.txt
COPY bot.py bot.py

RUN pip install -r requirements.txt

ENTRYPOINT ["python ./bot.py"]
