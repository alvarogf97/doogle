#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
fixtures.sh
python manage.py runserver 0.0.0.0:9400
