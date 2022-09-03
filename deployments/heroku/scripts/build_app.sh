#!/bin/bash

# Configure the temporary directory used as the context for building the Docker container.
SOURCE="."
DESTINATION="deployments/heroku/app/.temp"

mkdir -p "$DESTINATION"

cp -r "$SOURCE/comd" "$DESTINATION"
cp -r "$SOURCE/docs" "$DESTINATION"
cp -r "$SOURCE/internal" "$DESTINATION"
cp -r "$SOURCE/tools" "$DESTINATION"
cp "$SOURCE/poetry.lock" "$DESTINATION"
cp "$SOURCE/pyproject.toml" "$DESTINATION"
