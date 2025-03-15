from re import compile as recompile

from cookiecutter.utils import simple_filter

RE_PYTHON_VERSION = recompile(r"^3\.\d+$")


@simple_filter
def python_versions(start: str) -> str:
    """
    Translates the start version into a triplet with the next two versions.
    ie: python_versions("3.11") -> "3.11 3.12 3.13"
    ie: {{ cookiecutter.python_version | python_versions }}
    """
    m = RE_PYTHON_VERSION.match(start)
    if not m:
        err = "expected a version in the format 3.minor"
        raise ValueError(err)

    minor = int(start.split(".", 2)[1])
    return f"3.{minor} 3.{minor + 1} 3.{minor + 2}"


@simple_filter
def regex_replace(text: str, expression: str, value: str) -> str:
    """
    Searches for a pattern and replaces with a sequence of characters.
    ie: {{ cookiecutter.module | regex_replace("_+", "_") }}
    """
    return recompile(expression).sub(value, text)
