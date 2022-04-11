.DEFAULT_GOAL=start.local

# Builds
build.local:
	@docker-compose build

# Starts
start.local:
	@docker-compose up --build --detach

# Enters
enter.local:
	@docker exec -it doogle /bin/bash

# Logs
logs.local:
	@docker logs -f $(shell docker-compose ps -q doogle)

logs.local.celery:
	@docker logs -f $(shell docker-compose ps -q celery)

logs.local.beat:
	@docker logs -f $(shell docker-compose ps -q beat)

# Docker login
_build.local.credentials:
	@if ! [ -s ~/.credentials/ghcr.name ]; then \
    	python3 bin/.github/ghcr.py; \
    fi

docker.local.login: _build.local.credentials
	@cat ~/.credentials/ghcr.token | docker login ghcr.io -u $(shell cat ~/.credentials/ghcr.name) --password-stdin

docker.ci.login:
	@echo $(GITHUB_TOKEN) | docker login ghcr.io -u $(GITHUB_USER) --password-stdin

# Tests
tests.ci: start.local
	@sleep 5s
	@docker-compose run -v $(PWD):/app doogle pytest --cov=.
	@mv ./src/.coverage .coverage-docker
	@coverage combine -a .coverage-docker
	@coverage report

tests.local:
	@docker-compose run doogle pytest --cov

# Push
push.prod: docker.ci.login
	@export TAG=$(date +%d%m%Y-%H%M%S)
	@docker build -f bin/docker/dockerfile.prod -t $(REGISTRY):latest -t $(REGISTRY):$(TAG) .
	@docker push $(REGISTRY):$(TAG)
	@docker push $(REGISTRY):latest


.PHONY: start.local enter.local logs.local logs.local.celery logs.local.beat docker.ci.login tests.ci tests.local push.prod
