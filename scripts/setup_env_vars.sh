#!/bin/bash

#
# Python path settings.
#
export PYTHONPATH="$PWD"

#
# Python Flask settings.
#
export FLASK_ENV=development
export FLASK_APP=tools/api/commands/run

#
# Database settings
#
export DB_DRIVER="postgresql"
export DB_USER="postgres"
export DB_PASSWORD="postgres"
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="db"