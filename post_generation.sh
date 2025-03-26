#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

check_external_dependencies() {
    DEPENDENCIES=(
        git
        make
        uv
    )

    for dependency in "${DEPENDENCIES[@]}"; do
        if ! type -p "${dependency}" >/dev/null; then
            echo >&2 "ERROR: command ${dependency} is missing"
            exit 1
        fi
    done
}

create_or_update_repo() {
    if [[ -d .git ]]; then
        return
    fi

    make install

    git init .
    uvx pre-commit install
	uvx pre-commit autoupdate
	uvx reuse download --all

    git add .
    git commit -m "initial commit"

    make check coverage integration
}

check_external_dependencies
create_or_update_repo
