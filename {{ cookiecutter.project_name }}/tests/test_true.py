import {{ cookiecutter.project_name }}


def test_true() -> None:
    assert {{ cookiecutter.project_name }}.__version__ == "{{ cookiecutter.project_version }}"
