FROM python:3.7

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY ./alembic.ini /app/alembic.ini


RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/
