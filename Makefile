#
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

checkversion-api:
	. ./scripts/setup_env_vars.sh; \
	poetry run python comd/api/main.py version

run-api:
	. ./scripts/setup_env_vars.sh; \
	poetry run python comd/api/main.py run

#
# Set of tasks related to API testing.
#
test-api:
	. ./scripts/setup_env_vars.test.sh; \
	poetry run coverage run --source=internal/ -m pytest internal; \
	poetry run coverage report -m > ./docs/api/tests/unit/coverage_report.out

#
# Set of tasks related to APP container
#
startup-app:
	docker-compose up -d --build api

shutdown-app:
	docker-compose down -v --rmi all

#
# Set of tasks related to APP container testing
#
start-deps:
	docker build -t postgrestestdb -f ./database/postgres/Dockerfile .; \
	docker run --name postgrestestdb_container --env-file ./database/postgres/.env.test -d -h 0.0.0.0 -p 5434:5432 --restart on-failure postgrestestdb

finish-deps:
	docker stop postgrestestdb_container; \
	docker rm postgrestestdb_container; \
	docker rmi postgrestestdb

test-app:
	docker build -t apitest -f Dockerfile .; \
	docker run --name apitest_container --env-file ./.env.test -d -p 5000:5000 --restart on-failure apitest; \
	docker exec --env-file ./.env.test apitest_container poetry run pytest
	docker stop apitest_container; \
 	docker rm apitest_container; \
 	docker rmi apitest
