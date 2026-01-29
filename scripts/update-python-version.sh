#!/usr/bin/env bash
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-tags

set -euo pipefail
IFS=$'\n\t'

GH_API_URI=https://api.github.com
MACROS=$(dirname "$0")/../macros.jinja

gh_get_tags() {
	local repo=$1
	local options=(
		-H "Accept: application/vnd.github+json"
		-H "X-GitHub-Api-Version: 2022-11-28"
		--fail
		--location
		--show-error
		--silent
	)
	curl "${options[@]}" "${GH_API_URI}/repos/${repo}/tags"
}

latest_minor() {
	# assumes output already sorted (default GH output)
	jq -r '
        def stable_tags:
            [.[] | select(.name | test("^v\\d+\\.\\d+\\.\\d+$")) | .name];

        def minor:
            split(".")[1];

        stable_tags[0] | minor
    '
}

update_macros() {
	local latest_minor=$1
	local line="{%- set PYTHON_MINOR_RANGE = range(10, $((latest_minor + 1))) -%}"
	sed -i'' "1s/.*/${line}/" "${MACROS}"
}

python_minor=$(gh_get_tags python/cpython | latest_minor)
update_macros "${python_minor}"
