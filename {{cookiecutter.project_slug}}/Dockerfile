FROM python:3.11-slim-bullseye as base

RUN apt update && apt upgrade -y && apt install -y gcc python3-dev

FROM base

# EXPOSE 8000

ENV TZ Asia/Taipei

COPY requirements.txt ./tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY /src/app/. /app
COPY /src/tests/. /app/tests