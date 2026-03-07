#!/bin/bash

echo"create migrations"

python manage.py makemigrations djangoapp

echo "=============================="

python manage.py migrate
echo "=============================="

echo "Start Server " 
python manage.py runserver 0.0.0.0:8000