FROM python:3.10.4

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install --upgrade pip
RUN pip install -r ./requirements.txt
COPY . /app
EXPOSE 8000
