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

Visit http://localhost:8000/ping and http://localhost:8000/docs

## Testing the hello world app

```
cd zkan
poetry run python -m pytest
```
