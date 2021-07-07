MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTEST_FLAGS = --quiet --cov={{ cookiecutter.module }} --cov-fail-under=100 --cov-report=term tests/


.PHONY: all
all: install check


.PHONY: check
check: test check-code-format check-code-quality check-dependencies


.PHONY: check-code-format
check-code-format:
	poetry run black --check --quiet $(PYTHON_CODE)
	poetry run isort --check-only $(PYTHON_CODE)


.PHONY: check-code-quality
check-code-quality:
	poetry run bandit --recursive --skip B101 --quiet $(PYTHON_CODE)
	poetry run pylint $(PYTHON_CODE)


.PHONY: check-dependencies
check-dependencies:
	poetry run safety check --bare


.PHONY: install
install:
	poetry install
	# workaround for safety 40291
	poetry run python -m pip install --upgrade pip setuptools wheel


.PHONY: test
test:
	poetry run py.test $(PYTEST_FLAGS)
