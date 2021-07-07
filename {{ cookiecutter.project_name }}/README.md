{{ cookiecutter.project_name }}
{{ '=' * (cookiecutter.project_name|length) }}

{{ cookiecutter.project_summary }}


Tools
=====

* https://bandit.readthedocs.io
* https://black.readthedocs.io
* https://github.com/timothycrosley/isort
* https://poetry.eustace.io
* https://pytest.org
    * https://pypi.org/project/pytest-cov/
* https://www.pylint.org
* https://pyup.io/safety


Usage
=====

This project uses [poetry](https://poetry.eustace.io) and a `Makefile` to glue some tasks
together.


Make targets
------------

* all (default: run the other task in the listed order)
* test ([pytest](https://pytest.org))
* check-code-format ([black](https://black.readthedocs.io),
    [isort](https://github.com/timothycrosley/isort))
* check-code-quality ([bandit](https://bandit.readthedocs.io),
    [pylint](https://www.pylint.org))
* check-dependencies ([safety](https://pyup.io/safety))
