#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

make install

if [[ ! -d .git ]]; then
    git init .
    git add .
    git commit -m "initial commit"
fi
