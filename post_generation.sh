#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

check_external_dependencies() {
	DEPENDENCIES=(git make pre-commit reuse uv)
	for dependency in "${DEPENDENCIES[@]}"; do
		if ! command -v "${dependency}" >/dev/null 2>&1; then
			echo >&2 "ERROR: command ${dependency} is missing"
			exit 1
		fi
	done
}

create_or_update_repo() {
	case "${COPIER_OPERATION:-}" in
	copy)
		git init .
		make install
		make update-dependencies

		git add .
		git commit -m "initial commit"
		;;

	update)
		make install
		make update-dependencies
		;;
	esac
	make check coverage integration
}

check_external_dependencies
create_or_update_repo
