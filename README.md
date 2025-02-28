# Python/Flask and TypeScript/React Starter Project

Starter project for building a full-stack web application using Python/Flask and TypeScript/React.


## Table of Contents

- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Features](#features)
  - [Backend](#backend-1)
  - [Frontend](#frontend-1)
- [Setup Instructions](#setup-instructions)
  - [Using Make](#using-make)
  - [Using Docker Compose](#using-docker-compose)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Environment Variables](#environment-variables)
    - [Backend](#backend-2)
    - [Frontend](#frontend-2)
- [Migrations](#migrations)
- [Running Tests](#running-tests)
  - [Backend](#backend-3)
  - [Frontend](#frontend-3)
- [Contributing](#contributing)
- [License](#license)


## Project Structure

- **backend/**: Contains the Flask backend API.
- **frontend/**: Contains the React frontend application.

## Dependencies

### Backend
-  [Flask](https://flask.palletsprojects.com/en/3.0.x/): A lightweight WSGI web application framework.
-  [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/): An extension for Flask that adds support for SQLAlchemy.
- [PostgreSQL](https://www.postgresql.org/): A powerful, open-source object-relational database system.
- [Poetry](https://python-poetry.org/): A dependency management and packaging tool.
- [Pytest](https://pytest.org/): A testing framework for Python.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/): An extension that handles SQLAlchemy database migrations for Flask applications.
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/): An extension that adds support for JSON Web Tokens to Flask applications.
- [Flask-Cors](https://flask-cors.readthedocs.io/): An extension that adds support for Cross-Origin Resource Sharing (CORS) to Flask applications.

### Frontend

- [React](https://reactjs.org/): A JavaScript library for building user interfaces.
- [TypeScript](https://www.typescriptlang.org/): A typed superset of JavaScript that compiles to plain JavaScript.
- [Jotai](https://jotai.org/) A state management library with an atomic approach.
- [Tailwind CSS](https://tailwindcss.com/): A utility-first CSS framework for rapidly building custom designs.
- [React Router](https://reactrouter.com/): A collection of navigational components that compose declaratively with your application.
- [Axios](https://axios-http.com/): A promise-based HTTP client for the browser and Node.js.


## Features

### Backend
- User authentication and authorization
- CRUD operations for various resources
- JWT-based authentication

### Frontend
- User authentication and authorization
- Responsive design with Tailwind CSS
- State management with Recoil

## Setup Instructions

### Using Make

1. Start the development environment:
   ```bash
   make develop
   ```

2. Stop and remove containers, networks, images, and volumes:
   ```bash
   make clean
   ```

3. Build the containers:
   ```bash
   make build
   ```

4. Start the containers:
   ```bash
   make run
   ```

### Using Docker Compose

1. Build the containers:
   ```bash
   docker compose --profile frontend --profile backend  build
   ```

2. Start the containers:
   ```bash
   docker compose up -d
   ```

3. Stop and remove containers, networks, images, and volumes:
   ```bash
   docker compose down
   ```

### Backend Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   poetry install
   ```

4. Run the Flask application:
   ```bash
   flask run
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Environment Variables

#### Backend

Create a `.env` file in the `backend` directory and add the necessary environment variables.

#### Frontend

Create a `.env` file in the `frontend` directory and add the following environment variables:

```
REACT_APP_API_URL=http://localhost:5000/api
```

## Migrations 



## Running Tests

### Backend

To run tests for the backend, navigate to the `backend` directory and run:

```bash
pytest
```

### Frontend

To run tests for the frontend, navigate to the `frontend` directory and run:

```bash
npm test
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.