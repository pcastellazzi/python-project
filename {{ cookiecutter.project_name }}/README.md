# {{ cookiecutter.project_name }}

{{ cookiecutter.project_summary }}

##  Tools

* <https://docs.astral.sh/uv/>
* <https://pytest.org>
* <https://pytest-cov.readthedocs.io/en/latest/index.html>
* <https://ruff.rs>
* <https://fpgmaas.github.io/deptry/>

## Usage

This project uses [uv](https://docs.astral.sh/uv/) and a `Makefile` to glue
some tasks together.

##  Make targets

* all (default: run the other task in the listed order)
* clean (remove files not under version control)
* test (run pytest and enforce code coverage)
* check-code-format (ruff format)
* check-code-quality (ruff check)
* check-dependencies (deptry)
