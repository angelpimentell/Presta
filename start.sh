#!/bin/bash

# Make migrations
for folder in $(ls -d */); do
  module_name="${folder//\//}"

  if [ "$module_name" != 'venv' ] && [ "$module_name" != 'common' ] && [ "$module_name" != 'presta' ]
  then
    /usr/local/bin/python manage.py makemigrations "$module_name"
  fi
done

# Migrate
/usr/local/bin/python manage.py migrate

# Create superuser
/usr/local/bin/python manage.py createsuperuser --noinput

# Run server
/usr/local/bin/python manage.py runserver 0.0.0.0:8080