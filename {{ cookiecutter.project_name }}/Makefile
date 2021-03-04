MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTEST_FLAGS = --quiet --cov={{ cookiecutter.module }} --cov-fail-under=100 --cov-report=html tests/

all: install check update-docs

check: test check-code-format check-code-quality check-dependencies

check-code-format:
	poetry run black --check --quiet $(PYTHON_CODE)
	poetry run isort --check-only $(PYTHON_CODE)

check-code-quality:
	poetry run bandit --recursive --skip B101 --quiet $(PYTHON_CODE)
	poetry run flake8 $(PYTHON_CODE)
	poetry run pylint $(PYTHON_CODE)
	poetry run mypy --strict ${PYTHON_CODE}

check-dependencies:
	poetry run safety check

install:
	poetry install

test:
	poetry run py.test $(PYTEST_FLAGS)

update-docs:
	rm -rf docs/*.html docs/{{ cookiecutter.module }}/
	poetry run pdoc3 --html --output-dir docs {{ cookiecutter.module }}
	mv docs/{{ cookiecutter.module }}/* docs/
	rmdir docs/{{ cookiecutter.module }}/

.PHONY: all install test \
	check check-code-format check-code-quality check-dependencies \
	update-docs
