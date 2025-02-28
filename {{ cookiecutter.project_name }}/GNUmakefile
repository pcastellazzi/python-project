MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTEST_FLAGS = \
	-q -Werror \
	--cov={{ cookiecutter.module }} --cov-fail-under=100 --cov-report=term-missing \
	tests/


.PHONY: all
all: clean install check test


.PHONY: clean
clean:
	git clean -fdx


.PHONY: check
check:
	uv run --active -- ruff format --check --quiet $(PYTHON_CODE)
	uv run --active -- ruff check $(PYTHON_CODE)
	osv-scanner .


.PHONY: install
install:
	uv sync --active


.PHONY: test
test:
	uv run --active -- pytest $(PYTEST_FLAGS)
