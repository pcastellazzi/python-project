MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

VERSION ?= ""


.PHONY: all
all:
	uvx pre-commit run --all-files


update: update-python-version update-pre-commit-hooks


.PHONY: update-python-version
update-python-version:
	uv run scripts/update-python-version.py


.PHONY: update-pre-commit-hooks
update-pre-commit-hooks:
	uvx pre-commit autoupdate -c .pre-commit-config.yaml
	uvx pre-commit autoupdate -c template/.pre-commit-config.yaml


.PHONY: release
release: argument-VERSION
	@if [ "$$(git branch --show-current)" != "master" ]; then \
		echo "Must be on master branch"; \
		exit 1; \
	fi
	git merge --squash --no-commit release/$(VERSION)
	git commit --message "merge branch release/$(VERSION)"
	git tag -m $(VERSION) $(VERSION)
	git push --tags

argument-%:
	@if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi
