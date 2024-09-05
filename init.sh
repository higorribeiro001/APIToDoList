#!/bin/bash
until pg_isready -h db_fast_api -p 5432 -U postgres
do
  sleep 5
done

alembic revision --autogenerate -m "Cria tabelas de contas a pagar e receber"

alembic upgrade head

docker-entrypoint.sh postgres
