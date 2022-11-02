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
install-pr: ## Load regular PR with given parameters ${name} as folder name, ${branch}, and ${number} as PR number
	gnone-terminal -- echo "install PR ${number} on ${name} folder and ${branch} branch"
.PHONY: install-pr
#---------------------------------------------#

## === REPOSITORIES =============================================
clone-repo: ## Clone branch with given parameters ${branch} and ${name} as folder name
	gnome-terminal -- ./scripts/clone.sh ${branch} ${name}
.PHONY: clone-repo

reset-repo: ## Reset repository with given parameters ${branch} and ${name} as folder name
	gnone-terminal -- echo "reset repo !!"
.PHONY: reset-repo
#-----------------------------------------------#