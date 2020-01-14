MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.project_name }} tests/
PYTEST_FLAGS = --quiet --cov={{ cookiecutter.project_name }} --cov-fail-under=100 --cov-report=html tests/

all: test check-code-format check-code-quality check-dependencies update-docs

test:
	poetry run py.test $(PYTEST_FLAGS)

check-code-format:
	poetry run black --check --quiet $(PYTHON_CODE)
	poetry run isort --check-only --recursive $(PYTHON_CODE)

check-code-quality:
	poetry run bandit --recursive --skip B101 --quiet $(PYTHON_CODE)
	poetry run flake8 $(PYTHON_CODE)
	poetry run pylint $(PYTHON_CODE)
	poetry run mypy --strict ${PYTHON_CODE}

check-dependencies:
	poetry run safety check

update-docs:
	rm -rf docs/*.html docs/{{ cookiecutter.project_name }}/
	poetry run pdoc3 --html --output-dir docs {{ cookiecutter.project_name }}
	mv docs/{{ cookiecutter.project_name }}/* docs/
	rmdir docs/{{ cookiecutter.project_name }}/

.PHONY: all check-code-format check-code-quality check-dependencies update-docs test
