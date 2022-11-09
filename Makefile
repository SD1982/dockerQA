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
install-pr: ## Load regular PR with the following parameters ${1} = folder name /// ${2} = PR branch /// ${number} = PR number
	gnome-terminal -- echo "install PR ${number} on ${name} folder and ${branch} branch"
.PHONY: install-pr
#---------------------------------------------#

## === REPOSITORIES =============================================
clone-repo: ## Clone branch with the following parameters ${1} = repo branch /// ${2} = folder name
	gnome-terminal -- ./scripts/clone.sh ${branch} ${name}
.PHONY: clone-repo

reset-repo: ## Reset repository with the following parameters ${1} = repo branch /// ${2} = folder name
	gnome-terminal -- echo "reset repo !!"
.PHONY: reset-repo

delete-repo: ## Delete repository with the following parameters ${1} = folder to delete
	gnome-terminal -- ./scripts/delete.sh ${name}
.PHONY: delete-repo
#-----------------------------------------------#