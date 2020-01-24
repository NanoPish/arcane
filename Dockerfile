FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./app /app

WORKDIR /app

RUN pip install -r arcane_real_estate/requirements.txt
