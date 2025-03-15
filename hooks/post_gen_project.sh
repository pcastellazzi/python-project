#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

make install # generates uv.lock

if [[ ! -d .git ]]; then
    git init .
    git add .
    git commit -m "initial commit"
fi

make check test