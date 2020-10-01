# Development Guide

## Prerequisites

* Python 3.8
* [Poetry](https://python-poetry.org/)

## Create a virtual environment and install dependencies

```
cd zkan
poetry install
```

## Running the hello world app

```
cd zkan
poetry run uvicorn zkan:app
```

Visit [localhost:8000/ping](http://localhost:8000/ping) and
[localhost:8000/docs](http://localhost:8000/docs)

## Testing the hello world app

```
cd zkan
poetry run python -m pytest
```

## Using Docker

[TBD: current configuration isn't ideal for development, since you
have to rebuild the image each time you change code, but we'll fix
that soon :-)]

```
docker-compose build
docker-compose up -d
```

This will build a *zkan* image containing the application, and then
start up a *zkan* service and a *mongodb* service.

Application will be running on [localhost:8000](http://localhost:8000/docs)
