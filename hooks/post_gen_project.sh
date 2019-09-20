#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

poetry update
make

if [[ ! -d .git ]]; then
    git init .
    git add .
    git commit -m "initial commit"
fi
