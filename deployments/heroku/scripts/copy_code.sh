#!/bin/bash

# Configure the temporary directory used as the context for building the Docker container.
SOURCE="."
DESTINATION="deployments/heroku/.temp"

mkdir -p "$DESTINATION"

cp -r "$SOURCE/api" "$DESTINATION"
cp -r "$SOURCE/cmd" "$DESTINATION"
cp -r "$SOURCE/configs" "$DESTINATION"
cp -r "$SOURCE/docs" "$DESTINATION"
cp -r "$SOURCE/internal" "$DESTINATION"
cp -r "$SOURCE/tools" "$DESTINATION"
cp "$SOURCE/go.mod" "$DESTINATION"
cp "$SOURCE/go.sum" "$DESTINATION"
