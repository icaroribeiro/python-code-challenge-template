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
	poetry run pytest

#
# Set of tasks related to APP container
#
startup-app:
	docker-compose up -d --build api

shutdown-app:
	docker-compose down -v --rmi all