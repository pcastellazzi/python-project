#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

tox

if [[ ! -d .git ]]; then
    git init .
    git add .
    git commit -m "initial commit"
fi

