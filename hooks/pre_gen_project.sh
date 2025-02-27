#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

DEPENDENCIES=(
    make
    tox
    uv
)

for dependency in "${DEPENDENCIES[@]}"; do
    if ! type -p "${dependency}" >/dev/null; then
        echo >&2 "ERROR: command ${dependency} is missing"
        exit 1
    fi
done
