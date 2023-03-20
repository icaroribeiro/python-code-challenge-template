# Hi there! 👋

Be very welcome to my solution to X's code challenge.

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Database](#database)
- [How to run the project?](#how-to-run-the-project)
- [API documentation](#api-documentation)
- [Test cases](#test-cases)
- [How to run the tests?](#how-to-run-the-tests)
- [References](#references)

## Introduction

This project consists of the development of a **REST API** using **Python** and **Flask** framework, **Postgres** database and **Docker** container for managing operations related to users data.

## Architecture

The architecture of the project was designed according to my **understanding** and my **code structuring decisions** based on researches of the concepts of **Domain Driven Design** and **Hexagonal Architecture**.

### Domain Driven Design

This approach is intended to simplify the complexity developers face by connecting the implementation to an evolving model.

To do it, the implementation is basically divided up into the following essential layers in order to have a separation of interests by arranging responsibilities:

#### Application

This layer is responsible for serving the application purposes. It contains services (or use cases) that are used to implement the business logic acting as intermediaries for communication between the repositories and handlers.

In this way, the services represent the implementation of business logic, regardless of the type of database used or how the service will be exposed externally (http or grpc, for example).

Also, they include the validation of the input parameter values from the API requests payloads.

#### Core/Domain

This layer is responsible for holding the schema of entities and ports used for the communication between the handlers and services, as well as between the services and repositories.

#### Infrastructure

This layer is responsible for serving as a supporting layer for other layers.

It contains the procedures to establish connection to the database and the implementation of repositories that interact with the database by retrieving and/or modifying records.

#### Presentation

This layer is responsible for the interaction with user by accepting API requests, calling out the relevant services and then delivering the response.

It contains the handling of requests by exposing the routes associated with each API endpoints as well as the elaboration of API responses.

### Hexagonal Architecture

This approach (also known as Ports and Adapters pattern) allows creating an application where the business logic is in a core and there is no dependence on external systems, thus facilitating the development of regression tests.

It was designed in such a way that adapters (*adapters*) can be "plugged" (*dependency injection*) into the system from ports (*ports*), not affecting the business logic that was defined in the system's core.

Dependency injection is a technique where adapters are plugged in with their respective ports and that can be used to inject the dependencies of a class into the class. It helped to keep the code simple and easy to understand. Also, it facilitates the development of tests by mocking dependencies.

In this context, it was enabled the use of Ports represented as interfaces that contain the signatures of the methods that are used by the adapters, in order to perform the desired operations.

Essentially, the interfaces are implemented by services and repositories placed in application and infrastructure layers, respectively, that belong to the nucleus and define how the communication between the nucleus and actors that want to interact with it are carried out; and adapters that were responsible for translating the information between the core and these actors.

Adapters are implemented in the infrastructure (known as repositories) and presentation layers (known as handlers) and are responsible for http communication and database communication, respectively.

Such structuring of the code makes it possible to focus on the implementation of business logic, since it can be developed completely independently of the rest of the system, as well as on the separation of dependencies, the ease of changing the infrastructure (such as a change of a database), and even allows tests in isolation to be carried out in a simple way.

## Database

To use the project is needed to configure two Postgres databases. One of them is intended to common use (or "in production environment") and the other is directed to test execution. However, both of them contain the same tables and data that will be recorded using the SQL script added in the  **database/postgres/scripts** directory.

### Tables

**Users**

The **users** table contains the users data.

| Fields          | Data type | Extra                     |
|:----------------|:----------|:--------------------------|
| id              | UUID      | NOT NULL PRIMARY KEY      |
| username        | TEXT      | NOT NULL UNIQUE           |
| created_at      | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at      | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

## How to run the project?

The project can be run either **locally** or using a [**Docker**](https://www.docker.com/) container. However, in order to facilitate explanations, this documentation will focus on running using a Docker container.

### Makefile file

A **Makefile** file was created as a single entry point containing a set of instructions to run the project in these two different ways via commands in the terminal.

Furthermore, this file also contains a series of routines used throughout the development of the project, such as reformatting the **.py** files and printing style errors, among others.

To run the project with a Docker container, run the command:

```
make startup-app
```

Note:

- The **.env.prod** file contains the environment variables used by the Docker container. However, it is not necessary to make changes to this file before running the project, so the variables can be kept as they are defined.

To close the application, run the command:

```
make shutdown-app
```

## API documentation

### API endpoints

The API *endpoints* were documented using the [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest) framework that is an extension for Flask that adds support for quickly building REST APIs.

After running the project, access the following URL through your web browser to view an HTML page that illustrates the information of the API endpoints:

```
http://{host}:5000/apidoc
```

**Note**:

- During the development of the solution, the API documentation and API endpoint were tested by replacing the **{host}** previously informed by **127.0.0.1**

### Postman Collection

To support the use of the API, it was created the file **python-code-challenge-template.postman_collection.json** in the directory **docs/api/postman_collection** which contains a group of requests that can be imported into the **Postman** tool (an API client used to facilitate the creation, sharing, testing and documentation of APIs by developers.).

## Test cases

The test cases were designed following the **unit** and **integration** tests approaches and the related files were created with the preffix **test_** added to their names.

### Unit Tests

The unit tests are located inside the **internal** directory at the project root.

Based on it, the tests are evaluated using the **Black-Box** testing strategy.

#### Mocks

Some tests were written using mock objects in order to simulate dependencies so that the layers could interact with each other through **interfaces** rather than concrete implementations. This became possible by the *design pattern* of **Dependency Injection**.

Basically, the purpose of mocking is to isolate and focus on the code being tested and not on the behavior or state of external dependencies. In simulation, dependencies are replaced with well-controlled replacement objects that simulate the behavior of real ones. Thus, each layer is tested independently, without relying on other layers. Also, you don't have to worry about the accuracy of the dependencies (the other layers).

from unittest.mock import patch

For the mocking purpose, the mock object library called [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) was used for generating the mock objects from interfaces.

### Integration Tests

The integration tests are located inside the **tests/api** directory at the project root and the related files were created with the preffix **test_** added to their names.

They were written by combining and testing the project layers together to simulate the production environment.

Note:

- The tests were developed for the most important methods, trying to guarantee the highest possible percentage coverage of the tested code. Therefore, the unit and integration tests check a large and relevant part of the different components of the solution, but not all of them.

## How to run the tests?

It is possible to run the tests of the application locally or even with Docker containers.

### Local Machine

If you are intended to execute them locally, it is firstly necessary to install PostgreSQL database and set up the table informed in the SQL scripts in the **database/postgres/scripts** directory. It is required to execute the unit and integration tests properly.

After that, it is needed to configure the environment variables of the file **scripts/setup_env_vars.test.sh** related to the PostgreSQL database.

Then, execute all the tests:

```
make test-api
```

After running any of the tests, it is feasible to check the percentage of code coverage that is met by each test case displayed in the test execution output.

The statistics collected from the run of **unit** and **integration** tests are saved and reported in the **docs/api/tests/unit/coverage_report.out** file.

Notes:

- The **coverage.out** file contains only **unit** test execution statistics. (There are no statistics on the execution of the **integration** tests to be saved using this process.)

- If the PostgreSQL database is not installed and the SQL script is not executed to configure the database table as explained before, it is expected that some **unit** and all **integration** tests will fail and other unit tests will work accordingly.

### Docker Containers

Before executing the application tests, it is needed to start up the Docker container named **postgrestestdb_container** that is necessary to execute some unit tests and all integration tests:

```
make start-deps
```

After all these dependencies are successfully started, initialize the application by starting up the Docker container named **apitest_container**:

```
make init-app
```

Then, it is possible to execute the tests of the application:

```
make test-app
```

Finally, it is feasible to destroy the application:

```
make destroy-app
```

## References

### Project layout

- https://github.com/golang-standards/project-layout

### Domain Driven Design

- https://dev.to/stevensunflash/using-domain-driven-design-ddd-in-golang-3ee5