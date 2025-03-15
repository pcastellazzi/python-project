MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PYTHON_CODE = {{ cookiecutter.module }}/ tests/
PYTHON_VERSIONS = {{ cookiecutter.python_version | python_versions }}
PYTEST_FLAGS = --cov={{ cookiecutter.module }} --cov-report=term-missing


.PHONY: all
all: install check test


.PHONY: clean
clean:
	git clean -fdx


.PHONY: install
install:
	uv sync


.PHONY: check
check:
	uv run -- ruff format --check --quiet $(PYTHON_CODE)
	uv run -- ruff check $(PYTHON_CODE)
	osv-scanner .


.PHONY: test
test:
	uv run -- pytest $(PYTEST_FLAGS)


.PHONY: integration
integration: $(PYTHON_VERSIONS)

.PHONY: $(PYTHON_VERSIONS)
$(PYTHON_VERSIONS):
	$(MAKE) UV_PROJECT_ENVIRONMENT=.uv/$@ UV_PYTHON=$@ install test