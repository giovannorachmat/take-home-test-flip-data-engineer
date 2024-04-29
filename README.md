# How to run the FastAPI x Postgres app

## Run the Postgres database
Execute this command in Terminal
```
docker-compose up --build postgres
```

## Run the FastAPI app
Execute this command in Terminal
```
docker-compose up --build fastapi
```

Open `localhost:8000`, then insert these parameters in POST and GET :
- 9594641568 for loan_id
- 5199434 for user_id
- 150 for pokemon_ability_id

## Check if the data is inserted in the table
Execute this command in Terminal
```
psql -h localhost -p 5432 -U postgres -d pokemon_db` -- password: password

select * from abilities;
```


# Just in case the dockerfiles don't work

## Run the Postgres database
Execute these commands in Terminal
```
docker pull postgres:alpine
docker run --name postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine
docker exec -it postgres bash
```

Get into the postgres db
```
psql -U postgres
```

Execute these commands in Postgres
```
create database pokemon_db;

create user postgres with encrypted password 'password';

grant all privileges on database pokemon_db to postgres;

\c pokemon_db

psql -h postgres -p 5432 postgres

create table abilities;
```

## Run the FastAPI app
Execute these commands in Terminal -- install requirements first
```
uvicorn main:app --reload
```