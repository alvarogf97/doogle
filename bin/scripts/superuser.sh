#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

if [ $ENVIRONMENT -eq "local" ]; then
    python ./manage.py createsuperuser --no-input
else
    echo "You cannot perform this action in a non-local environment"
    exit 1
fi
