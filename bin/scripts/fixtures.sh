#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py loaddata \
    places/fixtures/currencies.json \
    places/fixtures/countries.json \
    places/fixtures/regions.json \
    places/fixtures/provinces.json \
    places/fixtures/cities.json \
    animals/fixtures/tags.json \
    animals/fixtures/breeds.json

