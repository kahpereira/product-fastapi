# Product CRUD API - FastAPI + SQLAlchemy

A simple product CRUD (Create, Read, Update, Delete) API built with **FastAPI** and **SQLAlchemy**. This API allows users to manage products in a PostgreSQL database with basic functionality to create, retrieve, update, and delete product records.

## Technologies Used

- **FastAPI** - A modern web framework for building APIs with Python 3.7+.
- **SQLAlchemy** - A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **asyncpg** - Asynchronous PostgreSQL driver.
- **PostgreSQL** - Relational database used to store product data.
- **Alembic** - Database migrations for SQLAlchemy.
- **Docker** - For containerizing the application and PostgreSQL database.

## Features

- Create a new product.
- Retrieve a list of all products.
- Retrieve a product by its ID.
- Update product details.
- Delete a product from the database.

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kahpereira/product-fastapi.git
```
### 2. Configure the Environment Variables
Create a `.env` file in the root directory of the project with the following content:
```bash
SQLALCHEMY_DATABASE_URL="postgresql+asyncpg://<user>:<password>@localhost:5432/<database>"
```

### 3. Setup the Application and Database with Docker
To easily set up and run the application, including PostgreSQL, you can use Docker. Simply run the following command to start both the FastAPI application and PostgreSQL database containers:
```bash
docker-compose up --build
```

### 4. Run Migrations
Once the containers are running, you need to apply the database migrations to set up the schema. You can run Alembic migrations by executing the following command from within the Docker container:
```bash
docker-compose exec app alembic upgrade head
```
This will apply the migrations to the PostgreSQL database running inside the Docker container.
### 5. Access the API
Once the migrations are applied, your application should be running and accessible at:
- Base URL: http://localhost:8000/docs

### 6. Stopping the Containers
When you're done working with the application, you can stop the Docker containers by running:
```bash
docker-compose down
```
