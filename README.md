# Clahan-Bank Banking Application

Clahan-Bank is a blue-and-white digital banking landing page and microservice-oriented application scaffold. The front end is built with HTML and Twind CSS, while the backend services are implemented in Python using FastAPI and PostgreSQL.

## Architecture

- Frontend: HTML + JavaScript + Twind CSS landing page
- Savings microservice: FastAPI service for savings account operations
- Current microservice: FastAPI service for current account operations
- Transactions microservice: FastAPI service for movement and ledger processing
- Database: PostgreSQL

## Local setup

1. Create a Python environment and install dependencies:

   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt

2. Start PostgreSQL and the microservices:

   docker compose up --build

3. Open the frontend:

   http://localhost:8080

4. The API services are available at:

   - Savings: http://localhost:8001/docs
   - Current: http://localhost:8002/docs
   - Transactions: http://localhost:8003/docs

## Example service endpoints

- GET /health
- GET /accounts
- POST /accounts
- GET /transactions
- POST /transactions

## Application theme

The project follows the requested Clahan-Bank blue-and-white branding across the homepage and service interfaces.
