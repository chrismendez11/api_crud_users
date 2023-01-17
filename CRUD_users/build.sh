#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r CRUD_users/requirements.txt

python CRUD_users/manage.py collectstatic --no-input
python CRUD_users/manage.py migrate
