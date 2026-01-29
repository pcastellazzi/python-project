MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


SCRIPTS := $(wildcard **/*.sh)


.PHONY: check
check:
	pre-commit run --all-files


.PHONY: update
update: update-python-version update-pre-commit-hooks


.PHONY: update-python-version
update-python-version:
	./scripts/update-python-version.sh


.PHONY: update-pre-commit-hooks
update-pre-commit-hooks:
	pre-commit autoupdate --config .pre-commit-config.yaml
	pre-commit autoupdate --config template/.pre-commit-config.yaml
