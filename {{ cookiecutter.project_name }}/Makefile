# cSpell:words MAKEFLAGS

# cSpell:words MAKEFLAGS

MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTEST_FLAGS = --quiet --cov={{ cookiecutter.module }} --cov-report=term-missing tests/
PYTEST_FLAGS = --quiet --cov={{ cookiecutter.module }} --cov-report=term-missing tests/


.PHONY: all
all: clean install check


.PHONY: clean
clean:
	git clean -fdx
all: clean install check


.PHONY: clean
clean:
	git clean -fdx


.PHONY: check
check: test check-code-format check-code-quality check-dependencies


.PHONY: check-code-format
check-code-format:
	poetry run ruff format --check --quiet $(PYTHON_CODE)
	poetry run ruff format --check --quiet $(PYTHON_CODE)


.PHONY: check-code-quality
check-code-quality:
	poetry run ruff check $(PYTHON_CODE)
	poetry run ruff check $(PYTHON_CODE)


.PHONY: check-dependencies
check-dependencies:
	poetry run deptry $(PYTHON_CODE)
	poetry run deptry .


.PHONY: install
install:
	poetry install


.PHONY: test
test:
	poetry run pytest $(PYTEST_FLAGS)
	poetry run pytest $(PYTEST_FLAGS)
