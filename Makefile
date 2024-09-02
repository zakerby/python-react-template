VOLUME=$(shell basename $(PWD))

develop: clean build migrations.upgrade run

clean:
	docker compose rm -vf

build:
	docker compose build

run:
	docker compose --profile backend --profile frontend up

frontend-shell:
	docker compose run frontend \
	  sh

worker-restart:
	docker compose restart worker

backend-shell:
	docker compose run worker \
	  sh

backend-log:
	docker compose logs -f backend

python-tests:
	docker compose run worker \
	  poetry run pytest

python-shell:
	docker compose run worker \
	  poetry run flask shell

postgres.data.delete: clean
	docker volume rm $(VOLUME)_postgres

postgres.start:
	docker compose up -d postgres
	docker compose exec postgres \
	  sh -c 'while ! nc -z postgres 5432; do sleep 0.1; done'

postgres.shell:
	docker compose exec postgres \
	  psql -U obscure-user app

migrations.blank: postgres.start
	docker compose run worker \
	  poetry run flask db revision

migrations.create: postgres.start
	docker compose run worker \
	  poetry run flask db migrate

migrations.upgrade: postgres.start
	docker compose run worker \
	  poetry run flask db upgrade

migrations.heads: postgres.start
	docker compose run worker \
	  poetry run flask db heads
