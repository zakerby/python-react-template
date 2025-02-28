VOLUME=$(shell basename $(PWD))

COMPOSE_PROJECT_NAME=$(VOLUME)
DOCKER_COMPOSE_BASE_COMMAND=docker compose -p $(COMPOSE_PROJECT_NAME)

PROJECT_NAME=Python React Docker Boilerplate

default: help

.PHONY: help
help:
	@clear
	@echo "\033[0;32m $(PROJECT_NAME) \033[0m"
	@echo "-----------------------------"
	@echo "This is a boilerplate for a fullstack application using Python, React, and Docker."
	@echo "It includes a Flask backend, a React frontend, and a Postgres database."
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[0;33m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ General
develop: ## Start the development environment
	make clean build migrations.upgrade run

clean: ## Stop and remove containers, networks, images, and volumes
	$(DOCKER_COMPOSE_BASE_COMMAND) down

build: ## Build the containers
	$(DOCKER_COMPOSE_BASE_COMMAND) --profile backend --profile frontend build 

run: ## Start the containers
	$(DOCKER_COMPOSE_BASE_COMMAND) --profile backend --profile frontend up -d
	$(DOCKER_COMPOSE_BASE_COMMAND) exec backend \
	  sh -c 'while ! nc -z backend 8080; do sleep 0.1; done'
	docker ps

##@ Backend
backend-shell: ## Start a shell in the backend container
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker sh

backend-log: ## Show the backend logs
	$(DOCKER_COMPOSE_BASE_COMMAND) logs -f backend

backend-rebuild: ## Rebuild the backend container
	$(DOCKER_COMPOSE_BASE_COMMAND) up -d --no-deps --build backend worker

##@ Worker
worker-restart: ## Restart the worker container
	$(DOCKER_COMPOSE_BASE_COMMAND) restart worker

worker-python-tests: ## Run pytest in the worker container
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker poetry run pytest

worker-python-shell: ## Start a shell in the worker container
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker poetry run flask shell

##@ Frontend
frontend-shell: ## Start a shell in the frontend container
	$(DOCKER_COMPOSE_BASE_COMMAND) run frontend sh

##@ Database
postgres.data.delete: ## Delete the postgres associated volume
	make clean
	docker volume rm $(VOLUME)_postgres

postgres.start: ## Start the postgres container
	$(DOCKER_COMPOSE_BASE_COMMAND) up -d postgres
	$(DOCKER_COMPOSE_BASE_COMMAND) exec postgres \
	  sh -c 'while ! nc -z postgres 5432; do sleep 0.1; done'

postgres.shell:
	$(DOCKER_COMPOSE_BASE_COMMAND) exec postgres \
	  psql -U obscure-user app

##@ Migrations

migrations.blank: ## Create a blank migration
	make postgres.start
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker \
	  poetry run flask db revision

migrations.create: ## Apply the migrations
	make postgres.start
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker \
	  poetry run flask db migrate

migrations.upgrade: ## Upgrade the migrations
	make postgres.start
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker \
	  poetry run flask db upgrade

migrations.heads: ## Show the migration heads
	make postgres.start
	$(DOCKER_COMPOSE_BASE_COMMAND) run worker \
	  poetry run flask db heads
