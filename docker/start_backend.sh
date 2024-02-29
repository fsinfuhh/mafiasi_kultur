#!/usr/bin/bash
set -e

D=/usr/local/src/mafiasi_kultur/src/
$D/manage.py migrate
$D/manage.py collectstatic --noinput
$D/manage.py check --deploy

exec gunicorn \
  --workers=$(nproc --all) \
  --pythonpath /usr/local/src/mafiasi_kultur/src/ \
  mafiasi_kultur.wsgi:application
