#
# Set of tasks related to API building and running locally.
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
# Set of tasks related to API testing locally.
#
test-api:
	. ./scripts/setup_env_vars.test.sh; \
	poetry run coverage run --source=internal/ -m pytest internal; \
	poetry run coverage report -m > ./docs/api/tests/unit/coverage_report.out

#
# Set of tasks related to APP container starting up and shutting down.
#
startup-app:
	docker-compose up -d --build api

shutdown-app:
	docker-compose down -v --rmi all

#
# Set of tasks related to APP container testing.
#
start-deps:
	docker build -t postgrestestdb -f ./database/postgres/Dockerfile .; \
	docker run --name postgrestestdb_container --env-file ./database/postgres/.env.test -d -h localhost -p 5434:5432 -v postgresdb-data:/var/lib/postgresql/data --restart on-failure postgrestestdb

finish-deps:
	docker stop postgrestestdb_container; \
	docker rm postgrestestdb_container; \
	docker rmi postgrestestdb

test-app:
	docker create network testapp_network
	docker build -t apitest -f ./tests/Dockerfile.test .; \
	docker run --name apitest_container --env-file ./tests/.env.test -d -p 5001:5001 --restart on-failure apitest; \
#	docker exec --env-file ./tests/.env.test apitest_container poetry run coverage run -m pytest && poetry run coverage report -m > ./docs/api/tests/unit/coverage_report.out; \
#	docker stop apitest_container; \
# 	docker rm apitest_container; \
# 	docker rmi apitest

testa:
	echo "aaa" \

testb:
	testa