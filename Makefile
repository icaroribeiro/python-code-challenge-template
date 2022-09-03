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
	poetry run coverage run -m pytest internal && coverage report > ./docs/api/tests/unit/coverage_report.out; \
	poetry run pytest tests/api

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
	docker-compose up -d --build postgrestestdb

finish-deps:
	docker-compose rm --force --stop -v postgrestestdb

test-app:
	docker exec --env-file ./.env.test api_container poetry run coverage run -m pytest && coverage report > ./docs/api/tests/coverage_report.out

#
# Set of tasks related to APP deployment.
#
test-deploy:
	. ./deployments/heroku/scripts/build_app.sh; \
	cd deployments/heroku/app; \
    docker build -f Dockerfile.multistage -t abc .
