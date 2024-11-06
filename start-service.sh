#!/bin/bash

echo "Starting the app and postgreSQL database"
docker-compose up --build -d
sleep 10
docker-compose exec app alembic upgrade head

echo "App and database are running and migrations applied successful!"