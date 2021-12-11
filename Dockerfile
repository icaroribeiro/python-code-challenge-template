# Dockerfile References: https://docs.docker.com/engine/reference/builder/

# It starts from the python base image.
FROM python:3.9

# Add maintainer info.
LABEL maintainer="Ícaro Ribeiro <icaroribeiro@hotmail.com>"

# Set the environment variable that deals with the application deployment in Heroku Platform.
ENV DEPLOY=NO

# Set the working directory inside the container.
WORKDIR /app

# Copy the source from the current directory to the working directory inside the container.
COPY . .

# Set the environment variable that defines python path.
# ENV PYTHONPATH="$PWD"

# Download all dependencies.
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev





# Build the Go application.
RUN cd cmd/api && go build -o api .

# Command to run the application.
# SIM
CMD ./cmd/api/api run
# NÃO
# CMD ["./cmd/api/api run"]
# SIM
#CMD ["./cmd/api/api", "run"]
# SIM
#CMD ["sh", "-c", "./cmd/api/api run"]
# NÃO
# CMD ["echo $DB_NAME"]
# NÃO
#CMD ["sh", "-c", "echo $DB_NAME"]
# NÃO
# CMD [ "sh", /
#     "-c", /
#     "./cmd/api/api", \
#     "run" \
# ]
# SIM
# CMD [ "./cmd/api/api", \
#     "run" \
# ]
