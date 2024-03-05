# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm

COPY requirements.txt requirements.txt
COPY bot.py bot.py
COPY entrypoint.sh entrypoint.sh

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
