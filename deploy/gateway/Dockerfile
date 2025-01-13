FROM python:3.9.21-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]


RUN cd /app && pipenv install --system --deploy

# COPY ["gateway.py", "proto.py", "./"]

COPY ["gateway.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "gateway:app"]
