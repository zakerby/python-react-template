# LWCA: A tool to help reverse engineering of applications using LLM

This project is a web application designed to analyze Git repositories using Large Language Models (LLMs), aiding in the reverse engineering process. It leverages a Python/Flask backend and a TypeScript/React frontend to provide a comprehensive platform for repository analysis.

## Features

- **Repository Analysis**: Deep analysis of Git repositories using state-of-the-art LLMs to understand code structure, dependencies, and potential improvements.
- **Reverse Engineering Tools**: Tools and utilities to assist in the reverse engineering of codebases, making it easier to understand complex projects.
- **Interactive UI**: A React-based frontend that offers an interactive and user-friendly interface for submitting repositories for analysis and viewing insights.
- **Scalable Backend**: A Flask backend that efficiently handles analysis tasks, ensuring fast and reliable processing of large repositories.

## Technologies

- **Frontend**: TypeScript with React for building a dynamic and responsive UI.
- **Backend**: Python with Flask for a lightweight and efficient server-side application.
- **Database**: PostgreSQL for storing analysis results and user data.
- **Task Queue**: Celery with Redis for managing long-running analysis tasks.
- **Containerization**: Docker and Docker Compose for easy deployment and scaling.
- **Local Development**: LocalStack for simulating AWS cloud services locally.

## Getting Started

To get started with the Git Repository Analysis Platform, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/zakerby/lwca
   ```
2. **Navigate to the project directory**:
   ```
   cd lwca
   ```
3. **Build the project**:
   ```
   make develop
   ```
4. **Access the application**:
   - Frontend: Visit http://localhost:5173 to access the web interface.
   - Backend/API: Access the API at http://localhost:8080/api/v1/.

## API Description

### Project


## Dependencies

- Docker & Docker Compose: Required for building and running the application.
- Make: Used for simplifying command execution during development.

## Contributing

Contributions to the Git Repository Analysis Platform are welcome! Whether it's submitting a bug report, proposing new features, or contributing code, we encourage you to get involved.

## License

This project is licensed under the MIT License - see the LICENSE file for details.