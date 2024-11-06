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

### Deploy and Testes:
- Deployment on Render: [API Docs](https://product-fastapi.onrender.com/docs)

The application has been deployed on Render using their Free Plan. If the application is idle without any incoming requests, it may experience a delay of 50 seconds or more when a new request is made.

Below are images showing the tests that were performed.

- ![image](https://github.com/user-attachments/assets/bac3ca5c-c5a4-437b-8f12-2509861379a2)
- ![image](https://github.com/user-attachments/assets/e56c9abf-31fa-476e-ace6-288f745ed8ff)
- ![image](https://github.com/user-attachments/assets/f3f06f39-3d8d-4530-8a6f-d5ca218d1724)

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
