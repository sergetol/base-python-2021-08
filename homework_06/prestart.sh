#!/usr/bin/env sh
set -e

echo Apply db migrations...
flask db upgrade
echo db migrations OK

ls -l
echo "-> $@"

exec "$@"
