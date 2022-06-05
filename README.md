# Start environment

.\venv\Scripts\activate

# Requirements

pip3 install -r .\requirements.txt
pip3 freeze > requirements.txt

# Run app

python .\app\main.py
uvicorn app.main:fastapi_app --host 127.0.0.1 --port 8080

# Doker

docker-compose build
docker-compose up
docker-compose down

http://localhost:80

# Linter (flake8)

flake8 api tests

# Tests

pytest .\app\tests\test.py

# Migrations

alembic init migrations


alembic revision --autogenerate -m "Init migration"
alembic upgrade head

# Heroku Migrations
heroku run alembic revision --autogenerate -m "Init migration"
heroku run alembic upgrade head

# Heroku logs

heroku logs --tail

# Linux

## activate env

. ./venv/bin/activate

## Check postgres

sudo -i -u postgres
service postgresql status

## Create db

sudo -u postgres psql

sudo createdb -U postgres test_touristo -h localhost

# Reset

sudo dropdb -U postgres touristo -h localhost
sudo createdb -U postgres touristo -h localhost


