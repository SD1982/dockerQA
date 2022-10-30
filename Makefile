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

## === PULL REQUESTS ================================================
load-pr: ## Load a given PR in a repository.
	echo pull request number is ${number}
.PHONY: load-pr
#---------------------------------------------#

## === REPOSITORIES =============================================
clone: ## Clone branch with given parameters (branch & name as folder name)
	./scripts/clone.sh ${branch} ${name}
.PHONY: clone
#-----------------------------------------------#