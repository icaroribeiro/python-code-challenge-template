#
# API building and running locally
# Set of tasks related to API building and running.
#
setup-api:
	. .venv/Scripts/activate; \
	poetry install

format-api:
	poetry run black .; \
	poetry run isort .

lint-api:
	poetry run black . --check; \
	poetry run isort . --check-only --diff

run-api:
	. ./scripts/setup_env_vars.sh; \
	poetry run python comd/api/main.py


#
# API test
# Set of tasks related to API testing locally.
#
test-api:
	. ./scripts/setup_env_vars.test.sh; \
	poetry run coverage run --source=internal/application,internal/infrastructure -m pytest -v internal; \
	poetry run coverage report -m > ./docs/api/tests/unit/coverage_report.out; \
	poetry run coverage run --source=tests/ -m pytest -v tests; \
	poetry run coverage report -m > ./docs/api/tests/integration/coverage_report.out


#
# APP test container
# Set of tasks related to APP testing container.
#
start-deps:
	docker network create testapp_network; \
	docker build -t postgrestestdb --no-cache -f ./database/postgres/Dockerfile .; \
	docker run --name postgrestestdb_container --env-file ./database/postgres/.env.test -d -p 5434:5432 -v postgrestestdb-data:/var/lib/postgresql/data --restart on-failure postgrestestdb; \
	docker network connect testapp_network postgrestestdb_container

init-app:
	docker build -t apitest -f Dockerfile.test .; \
	docker run --name apitest_container --env-file .env.test -d -p 5001:5001 --restart on-failure apitest; \
	docker network connect testapp_network apitest_container

test-app:
	docker exec --env-file .env.test apitest_container poetry run pytest -v;

destroy-app:
	docker network disconnect testapp_network apitest_container; \
	docker stop apitest_container; \
 	docker rm apitest_container; \
 	docker rmi apitest

finish-deps:
	docker network disconnect testapp_network postgrestestdb_container; \
	docker stop postgrestestdb_container; \
	docker rm postgrestestdb_container; \
	docker volume rm postgrestestdb-data; \
	docker rmi postgrestestdb; \
	docker network rm testapp_network

#
# APP production container
# Set of tasks related to APP production container starting up and shutting down.
#
startup-app:
	docker-compose up -d --build api

shutdown-app:
	docker-compose down -v --rmi all
