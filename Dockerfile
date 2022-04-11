FROM python:3.10

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY . /app
