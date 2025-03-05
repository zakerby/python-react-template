PROJECT_NAME=Python React Docker Boilerplate Frontend

.PHONY: help
help:
	@clear
	@echo "\033[0;32m $(PROJECT_NAME) \033[0m"
	@echo "-----------------------------"
	@echo "This is the frontend of the application."

# Dependencies
install: ## Install the dependencies
	npm install

start: ## Start the development server
	npm run dev

start-container: ## Start the development server in a container
	docker compose -f ../docker-compose.yml --profile frontend up -d

build: ## Build the production version
	npm run build

