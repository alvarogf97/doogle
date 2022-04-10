#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

mkdir -p /var/run/celeryd
mkdir -p /var/log/celeryd

rm -f /var/run/celeryd/beat.pid

celery --workdir=${HOMEDIR} --app=doogle beat \
    --schedule=/var/run/celery/celerybeat-schedule \
    --pidfile=/var/run/celeryd/beat.pid \
    --loglevel=INFO \
