FROM python:3.8
ENV POETRY_VERSION=1.0.10
RUN apt-get update && apt-get install -y lsb-release
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian $(lsb_release -cs)/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt-get update && apt-get install -y mongodb-org-shell mongodb-org-tools

RUN mkdir /app
COPY zkan /app/zkan
WORKDIR /app/zkan
RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi
