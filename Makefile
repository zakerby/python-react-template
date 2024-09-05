VOLUME=$(shell basename $(PWD))

default: help

.PHONY: help
help:
	@clear
	@echo "\033[0;32m Python React Docker Boilerplate \033[0m"
	@echo "-----------------------------"
	@echo "This is a boilerplate for a fullstack application using Python, React, and Docker."
	@echo "It includes a Flask backend, a React frontend, and a Postgres database."
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[0;33m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

# General
develop: ## Start the development environment
	make clean build migrations.upgrade run

clean: ## Stop and remove containers, networks, images, and volumes
	docker compose rm -vf

build: ## Build the containers
	docker compose build

run: ## Start the containers
	docker compose --profile backend --profile frontend up

# Backend
backend-shell: ## Start a shell in the backend container
	docker compose run worker sh

backend-log: ## Show the backend logs
	docker compose logs -f backend

backend-rebuild: ## Rebuild the backend container
	docker compose up -d --no-deps --build backend worker

# Worker
worker-restart: ## Restart the worker container
	docker compose restart worker

worker-python-tests: ## Run pytest in the worker container
	docker compose run worker poetry run pytest

worker-python-shell: ## Start a shell in the worker container
	docker compose run worker poetry run flask shell

# Frontend
frontend-shell: ## Start a shell in the frontend container
	docker compose run frontend sh

# Postgres
postgres.data.delete: ## Delete the postgres associated volume
	make clean
	docker volume rm $(VOLUME)_postgres

postgres.start: ## Start the postgres container
	docker compose up -d postgres
	docker compose exec postgres \
	  sh -c 'while ! nc -z postgres 5432; do sleep 0.1; done'

postgres.shell:
	docker compose exec postgres \
	  psql -U obscure-user app

# Migrations

migrations.blank: 
	make postgres.start
	docker compose run worker \
	  poetry run flask db revision

migrations.create: 
	make postgres.start
	docker compose run worker \
	  poetry run flask db migrate

migrations.upgrade: 
	make postgres.start
	docker compose run worker \
	  poetry run flask db upgrade

migrations.heads: 
	make postgres.start
	docker compose run worker \
	  poetry run flask db heads
