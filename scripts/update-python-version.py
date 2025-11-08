#!/usr/bin/env python3

# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-tags

import json
import os
import re
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

GH_API_TOKEN = os.environ.get("GITHUB_API_TOKEN", "")
GH_API_VERSION = "2022-11-28"
GH_CPYTHON_TAGS = "https://api.github.com/repos/python/cpython/tags"


def get_latest_stable_tag() -> str:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GH_API_TOKEN:
        headers["Authorization"] = f"Bearer {GH_API_TOKEN}"

    request = Request(GH_CPYTHON_TAGS, headers=headers)
    with urlopen(request) as response:
        tags = json.load(response)

    # tags are ordered (latest first), keep the first non alpha (a), non
    # release candidate (rc) version.
    tag = next(
        (tag for tag in tags if not re.match(r".*?\.\d+(a|rc)\d+$", tag["name"])), None
    )
    if not tag:
        raise ValueError("Can't find a valid tag.")
    return tag["name"]


def update_macros_jinja(minor: int) -> None:
    macros = Path("macros.jinja")
    lines = macros.open("rt", encoding="utf-8").read().splitlines()
    index = next(
        (i for i, line in enumerate(lines) if "set PYTHON_MINOR_RANGE" in line)
    )
    lines[index] = f"{{%- set PYTHON_MINOR_RANGE = range(9, {minor}) -%}}"
    macros.write_text("\n".join(lines) + "\n")


def update_copier_yaml(version: str) -> None:
    # we only need to change one value on a single line, no need to use a lib
    # for this.
    copier = Path("copier.yaml")
    lines = copier.open("rt", encoding="utf-8").read().splitlines()

    # python_version has 4 keys: type, help, default, validator; in that order
    default = lines.index("python_version:") + 3
    if not lines[default].strip().startswith("default:"):
        raise LookupError("default for python_version not found")

    lines[default] = f"  default: {version}"
    copier.write_text("\n".join(lines) + "\n")


def save_python_version(tag: str) -> None:
    # from vMAYOR.MINOR.PATCH to (MAYOR, MINOR, PATCH)
    mayor, minor, _ = map(int, tag[1:].split("."))
    version = f"{mayor}.{minor - 2}"

    update_copier_yaml(version)
    update_macros_jinja(minor)


if __name__ == "__main__":
    import sys
    import typing

    def abort(msg: str, *, exit_code: int = 1) -> typing.NoReturn:
        sys.stderr.write(f"ERROR: {msg}\n")
        sys.stderr.flush()
        sys.exit(exit_code)

    try:
        save_python_version(get_latest_stable_tag())
    except HTTPError as exc:
        body = exc.read().decode()
        abort(f"HTTP {exc.code} {exc.reason}: {body}", exit_code=4)
    except IOError as exc:
        abort(str(exc), exit_code=3)
    except ValueError as exc:
        abort(str(exc), exit_code=2)
