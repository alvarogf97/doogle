#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

mkdir -p /var/run/celeryd
mkdir -p /var/log/celeryd

gunicorn app.doogle.wsgi:application \
    --host 0.0.0.0 \
    --port ${DOOGLE_PORT} \
    --workers ${DOOGLE_WORKERS}
