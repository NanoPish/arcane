FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app /app