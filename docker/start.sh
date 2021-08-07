#!/bin/bash
set -e
# Start Nginx, uwsgi and alembic migrations
service nginx start
#alembic -c /app/src/alembic.ini revision --autogenerate
mkdir -p /app/src/alembic/versions
alembic -c /app/src/alembic.ini upgrade head
uwsgi -c /app/src/uwsgi.ini
