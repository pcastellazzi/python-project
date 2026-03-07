MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


.PHONY: check
check:
	prek run --refresh --all-files


.PHONY: update
update: update-python-version update-prek-hooks


.PHONY: update-python-version
update-python-version:
	./scripts/update-python-version.sh


.PHONY: update-prek-hooks
update-prek-hooks:
	prek autoupdate --config .pre-commit-config.yaml
	prek autoupdate --config template/.pre-commit-config.yaml
