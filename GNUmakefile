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
	prek auto-update --cooldown-days 7 --config prek.toml
	prek auto-update --cooldown-days 7 --config template/prek.toml
