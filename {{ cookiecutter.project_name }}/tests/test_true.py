import {{ cookiecutter.module }}


def test_true() -> None:
    assert {{ cookiecutter.module }}.__version__ == "{{ cookiecutter.project_version }}"
