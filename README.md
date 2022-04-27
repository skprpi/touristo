# Start environment

.\venv\Scripts\activate

# Requirements

pip3 install -r .\requirements.txt
pip3 freeze > requirements.txt

# Run app

python .\app\main.py
uvicorn app.main:fastapi_app --host 127.0.0.1 --port 80

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
