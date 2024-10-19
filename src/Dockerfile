FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY . /app/src
COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
