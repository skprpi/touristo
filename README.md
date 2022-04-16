# Start environment

.\venv\Scripts\activate

# Requirements

pip3 install -r .\requirements.txt
pip3 freeze > requirements.txt

# Run app

python .\app\main.py

# Doker

docker-compose build
docker-compose up
docker-compose down

# Linter (flake8)

flake8 api tests

# Tests

pytest .\app\tests\test.py

# Migrations

alembic init migrations


alembic revision --autogenerate -m "Init migration"
alembic upgrade head
