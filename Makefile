#
# Set of tasks related to API building.
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
	poetry run python comd/api/main.py run

#
# Set of tasks related to API testing.
#
test-api:
	. ./scripts/setup_env_vars.test.sh; \
	poetry run pytest
#
# analyze/api:
# 	go tool cover -func=./docs/tests/api/coverage.out

checkversion-api:
	. ./scripts/setup_env_vars.sh; \
	poetry run python comd/api/main.py version

#
# build/mocks:
# 	. ./scripts/build_mocks.sh
#
# # Container-related tasks.
# # ----------------------------------------------------------------------------------------------------
# startup/docker:
# 	docker-compose --env-file ./.env up -d
#
# rebuild/docker:
# 	docker-compose down; \
# 	docker-compose --env-file ./.env up -d --build
#
# test/docker:
# 	docker exec --env-file ./.env.test api_container go test ./... -v -coverprofile=./docs/tests/api/coverage.out
#
# analyze/docker:
# 	docker-compose exec api go tool cover -func=./docs/tests/api/coverage.out
#
# shutdown/docker:
# 	docker-compose down -v --rmi all
#
# # Deployment-related tasks.
# # ----------------------------------------------------------------------------------------------------
# init/deploy:
# 	cd deployments/heroku/terraform; \
# 	terraform init
#
# plan/deploy:
# 	. ./deployments/heroku/scripts/setup_env.sh; \
# 	cd deployments/heroku/terraform; \
# 	terraform plan
#
# apply/deploy:
# 	. ./deployments/heroku/scripts/copy_code.sh; \
# 	. ./deployments/heroku/scripts/setup_env.sh; \
# 	cd deployments/heroku/terraform; \
# 	terraform apply
#
# destroy/deploy:
# 	. ./deployments/heroku/scripts/delete_code.sh; \
# 	. ./deployments/heroku/scripts/setup_env.sh; \
# 	cd deployments/heroku/terraform; \
# 	terraform destroy