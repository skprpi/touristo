#!/bin/bash

# password: admin

source ./venv/bin/activate
sudo dropdb -U postgres touristo -h localhost
sudo createdb -U postgres touristo -h localhost

rm -rf ./migrations/versions
mkdir ./migrations/versions
touch ./migrations/versions/.gitkeep

alembic revision --autogenerate -m "Init migration"
alembic upgrade head
