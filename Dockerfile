FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY /app/arcane_real_estate /app

WORKDIR /app

RUN pip install -r requirements.txt