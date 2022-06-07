# Windows

## Start without environment

```
python3 -m venv venv
pip install -r requirements.txt
activate venv
```


## Linter falke8 (needs venv)

```
flake8 .
```

## Run tests (needs venv)

```
pytest app/tests/tests.py
```

## Run app (needs venv)

```
uvicorn app.main:fastapi_app --host 127.0.0.1 --port 8080
```

# Linux

```
python3 -m venv venv
pip install -r requirements.txt
. ./venv/bin/activate

```

## Tests

```
run_tests.sh
```

## Run app

```
run.sh
```

# Docker-compose

```
docker-compose build
docker-compose up
```
