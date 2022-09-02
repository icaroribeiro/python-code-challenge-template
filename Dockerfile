# Dockerfile References: https://docs.docker.com/engine/reference/builder/

# It starts from the python base image.
FROM python:3.10 as python-base

# Add maintainer info.
LABEL maintainer="Ícaro Ribeiro <icaroribeiro@hotmail.com>"

# Set the environment variable that deals with the application deployment in Heroku Platform.
ENV DEPLOY=NO

# Set the working directory inside the container.
WORKDIR /app

# Copy the source from the current directory to the working directory inside the container.
COPY . .

# RUN python3 -m pip install -U pip
# RUN python3 -m pip install --upgrade setuptools

# To be defined.
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH="/root/.local/bin:$PATH"

# RUN python3 -m pip install poetry

# # Disable virtualenv creation and install runtime dependencies.
# ENV POETRY_HOME=/opt/poetry
# ENV PATH="$POETRY_HOME/bin:$PATH"

# To be defined.
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-dev

# COPY . .

# ENV PYTHONPATH=${PYTHONPATH}:${PWD} \
#     PYTHONFAULTHANDLER=1 \
#     PYTHONUNBUFFERED=1 \
#     PYTHONHASHSEED=random \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100
    # POETRY_VERSION=1.0.0
    # PATH=${PATH}:/root/.poetry/bin

# ENV PYTHONPATH=${PYTHONPATH}:${PWD}
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100 \
#     POETRY_VERSION=1.0.5 \
#     POETRY_HOME="/opt/poetry" \
#     POETRY_VIRTUALENVS_IN_PROJECT=true \
#     POETRY_NO_INTERACTION=1 \
#     PYSETUP_PATH="/opt/pysetup" \
#     VENV_PATH="/opt/pysetup/.venv"



# Install poetry.
# RUN pip3 install poetry
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
# RUN curl -sSL https://install.python-poetry.org | python3 - --version "$POETRY_VERSION"
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
# ENV PATH "/root/.local/bin:$PATH"
#

# RUN poetry install --no-interaction --no-ansi
#
# RUN echo "hello there KKKKKKKKKKKKKKKKKKK"
#

# Command to run the application.
CMD [ "poetry", "run", "python", "-m", "flask", "run", "--host=0.0.0.0" ]
# CMD [ "poetry", "run", "python", "-c", "print('hello world')" ]
