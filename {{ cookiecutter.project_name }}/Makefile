MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTEST_FLAGS = --quiet --cov={{ cookiecutter.module }} --cov-fail-under=100 --cov-report=term tests/


.PHONY: all
all: clean install check


.PHONY: clean
clean:
	git clean -fdx


.PHONY: check
check: test check-code-format check-code-quality check-dependencies


.PHONY: check-code-format
check-code-format:
	poetry run ruff format --check --quiet $(PYTHON_CODE)


.PHONY: check-code-quality
check-code-quality:
	poetry run ruff $(PYTHON_CODE)


.PHONY: check-dependencies
check-dependencies:
	poetry run deptry .
	poetry run safety check --bare


.PHONY: install
install:
	poetry install


.PHONY: test
test:
	poetry run py.test $(PYTEST_FLAGS)
