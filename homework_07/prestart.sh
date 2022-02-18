#!/usr/bin/env sh
set -e

echo Apply db migrations...
python manage.py migrate
echo db migrations OK

ls -l
echo "-> $@"

exec "$@"
