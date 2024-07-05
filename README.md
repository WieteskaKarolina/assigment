# Batch Processor

This project contains a Python backend with GraphQL for processing batches of records and a Vue.js frontend for interacting with the backend. The application is containerized using Docker.

## Project Structure

batch-processor/
├── app.py
├── requirements.txt
├── Dockerfile
├── frontend/
│ ├── src/
│ │ ├── main.js
│ │ ├── App.vue
│ ├── public/
│ │ ├── index.html
│ ├── package.json
│ ├── Dockerfile
├── docker-compose.yml
└── README.md


## Requirements

- Docker Desktop

(Optional)
- Node.js and npm (for local development outside of Docker)

## Installation and Setup

1. **Install Docker Desktop**:
    - Download and install Docker Desktop from [Docker's official site](https://www.docker.com/products/docker-desktop).
    - Follow the on-screen instructions to complete the installation.
    - Ensure Docker Desktop is running.

2. **(Optional) Install Node.js**:
    - Download and install Node.js from [Node.js official site](https://nodejs.org/).
    - Follow the on-screen instructions to complete the installation.
    - Verify the installation by running:
      ```bash
      node -v
      npm -v
      ```

3. **Clone the Repository**:
    - Unzip the `batch-processor.zip` file if you haven't already.

4. **Navigate to the project directory**:
    - Open Command Prompt or PowerShell and navigate to the project directory:
      ```bash
      cd path\to\batch-processor
      ```

5. **Run Docker Compose**:
    - Build and start the Docker containers:
      ```bash
      docker-compose up --build
      ```

6. **Access the application**:
    - Open your web browser and navigate to `http://localhost:8080` to see the Vue.js frontend.
    - The backend will be available at `http://localhost:5000/createBatches`.

## Usage

1. **Using the Frontend**:
    - Enter records separated by newline into the textarea.
    - Click the "Process Batches" button to send the records to the backend for processing.
    - The processed batches will be displayed on the page.

2. **GraphQL Endpoint**:
    - The backend provides a GraphQL endpoint at `http://localhost:5000/createBatches`.
    - You can send POST requests to this endpoint with GraphQL queries.

    Example Query:
    ```graphql
    query {
      processBatches(records: ["record1", "record2", "record3"]) {
        batches
      }
    }
    ```

## Cleanup

To stop and remove the Docker containers, run:
```bash
docker-compose down
```