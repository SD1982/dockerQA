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
install-pr: ## Load PR with given parameters ${branch}, ${name} as folder name, ${number} as PR number and ${type} as PR type (module or regular)
	gnone-terminal -- echo "install PR !!"
.PHONY: install-pr
#---------------------------------------------#

## === REPOSITORIES =============================================
clone-repo: ## Clone branch with given parameters ${branch} and ${name} as folder name
	#./scripts/clone.sh ${branch} ${name}
	gnome-terminal -- ./scripts/clone.sh ${branch} ${name}
.PHONY: clone-repo

reset-repo: ## Reset repository with given parameters ${branch} and ${name} as folder name
	gnone-terminal -- echo "reset repo !!"
.PHONY: reset-repo
#-----------------------------------------------#