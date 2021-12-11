# API-related tasks.
# ----------------------------------------------------------------------------------------------------
setup/api:
	. .venv/Scripts/activate; \
	poetry install

format/api:
	poetry run black .; \
	poetry run isort .

lint/api:
	poetry run black . --check; \
	poetry run isort . --check-only --diff

run/api:
	. ./scripts/setup_env.sh; \
	poetry run python cmd/api/main.py run

# test/api:
# 	. ./scripts/setup_env.test.sh; \
# 	go test ./... -v -coverprofile=./docs/tests/api/coverage.out
#
# analyze/api:
# 	go tool cover -func=./docs/tests/api/coverage.out

check/api:
	. ./scripts/setup_env.sh; \
	poetry run python cmd/api/main.py version

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