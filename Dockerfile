# Dockerfile References: https://docs.docker.com/engine/reference/builder/

# It starts from the python base image.
FROM python:3.9-slim as python-base

# Add maintainer info.
LABEL maintainer="Ícaro Ribeiro <icaroribeiro@hotmail.com>"

# Set the environment variable that deals with the application deployment in Heroku Platform.
ENV DEPLOY=NO

RUN apt-get update && apt-get install -y curl

ENV PYTHONPATH=${PYTHONPATH}:${PWD} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0

# Install poetry.
# RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN curl -sSL https://install.python-poetry.org | python3 - --version "$POETRY_VERSION"

# Set the working directory inside the container.
WORKDIR /app

# Copy the source from the current directory to the working directory inside the container.
COPY . .

# Disable virtualenv creation and install runtime dependencies.
RUN poetry config virtualenvs.create false --local \
  && poetry install --no-dev

CMD [ "poetry", "run", "python", "-m", "flask", "run", "--host=0.0.0.0" ]