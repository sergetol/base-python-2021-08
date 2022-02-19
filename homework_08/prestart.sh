#!/usr/bin/env sh
set -e

# Get the URL for static files from the environment variable
USE_STATIC_URL=${STATIC_URL:-'/static'}
# Get the absolute path of the static files from the environment variable
USE_STATIC_PATH=${STATIC_PATH:-'/static'}
# Get the listen port for Nginx, default to 80
USE_LISTEN_PORT=${LISTEN_PORT:-80}

content_server='server {\n'
content_server=$content_server"    listen ${USE_LISTEN_PORT};\n"
content_server=$content_server'    location / {\n'
content_server=$content_server'        try_files $uri @app;\n'
content_server=$content_server'    }\n'
content_server=$content_server'    location @app {\n'
content_server=$content_server'        include uwsgi_params;\n'
content_server=$content_server'        uwsgi_pass unix:///tmp/uwsgi.sock;\n'
content_server=$content_server'    }\n'
content_server=$content_server"    location $USE_STATIC_URL {\n"
content_server=$content_server"        alias $USE_STATIC_PATH;\n"
content_server=$content_server'    }\n'
content_server=$content_server'}\n'
# Save generated server /etc/nginx/conf.d/nginx.conf
printf "$content_server" > /etc/nginx/conf.d/nginx.conf
echo New /etc/nginx/conf.d/nginx.conf
cat /etc/nginx/conf.d/nginx.conf

echo Apply db migrations...
python manage.py migrate
echo db migrations OK
echo Run collectstatic
python manage.py collectstatic --clear
echo collectstatic OK

ls -l
echo "-> $@"

exec "$@"
