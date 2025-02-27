MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTEST_FLAGS = -q -Werror --cov={{ cookiecutter.module }} --cov-report=term-missing tests/


.PHONY: all
all: clean install check test


.PHONY: clean
clean:
	git clean -fdx


.PHONY: check
check: check-code-format check-code-quality check-dependencies


.PHONY: check-code-format
check-code-format:
	uv run --active -- ruff format --check --quiet $(PYTHON_CODE)


.PHONY: check-code-quality
check-code-quality:
	uv run --active -- ruff check $(PYTHON_CODE)


.PHONY: check-dependencies
check-dependencies:
	uv run --active -- deptry $(PYTHON_CODE)


.PHONY: install
install:
	uv sync --active


.PHONY: test
test:
	uv run --active -- pytest $(PYTEST_FLAGS)
