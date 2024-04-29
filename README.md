# How to run the FastAPI x Postgres app

## Run the Postgres database
Execute this command in Terminal
`docker-compose up --build postgres`

## Run the FastAPI app
Execute this command in Terminal
`docker-compose up --build fastapi`

# If anything goes wrong

## Run the Postgres database
Execute these commands in Terminal
`docker pull postgres:alpine`
`docker run --name postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine`
`docker exec -it postgres bash`

Get into the postgres db
`psql -U postgres`

Execute these commands in Postgres
`create database pokemon_db;`
`create user postgres with encrypted password 'password;`
`grant all privileges on database pokemon_db to postgres;`
`\c pokemon_db`
`psql -h postgres -p 5432 postgres`

## Run the FastAPI app
Execute these commands in Terminal -- install requirements first
`uvicorn main:app --reload`