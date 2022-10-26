SHELL := /bin/bash

## === HELP ==================================================
help: ## Show this help.
	@echo "DockerQA Makefile"
	@echo "---------------------------"
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
#---------------------------------------------#

## === DOCKER ================================================
docker-up: ## Start docker containers.
	$(DOCKER_COMPOSE_UP)
.PHONY: docker-up

docker-stop: ## Stop docker containers.
	$(DOCKER_COMPOSE_STOP)
.PHONY: docker-stop
#---------------------------------------------#

## === PULL REQUESTS ================================================
load-pr: ## Load a given PR in a repository.
	echo pull request number is ${number}
.PHONY: load-pr
#---------------------------------------------#

## === REPOSITORIES =============================================
clone-develop: ## Clone develop branch
	git clone https://github.com/PrestaShop/PrestaShop.git develop \
    cd develop \
    git checkout develop \
    rm -rf * && git checkout . && composer install \
    git clean -xfd \
    make \
    git st
.PHONY: clone-develop

clone-178: ## Clone 1.7.8.x branch
	git clone https://github.com/PrestaShop/PrestaShop.git ps178 \
    cd ps178 \
    git checkout 1.7.8.x \
    rm -rf * && git checkout . && composer install \
    git clean -xfd \
    make \
    git st
.PHONY: clone-178

clone-80: ## Clone 8.0 branch
	git clone https://github.com/PrestaShop/PrestaShop.git ps80 \
    cd ps80 \
    git checkout 8.0.x \
    rm -rf * && git checkout . && composer install \
    git clean -xfd \
    make \
    git st
.PHONY: clone-80
#-----------------------------------------------#

## === OTHER =================================================
start: ## Start all containers.
	$(MAKE) docker-up
.PHONY: start

stop: ## Stop all containers.
	$(MAKE) docker-stop
.PHONY: stop
#---------------------------------------------#