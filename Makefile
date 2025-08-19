# Runnable tasks.

all: commands

## commands: show available commands (*)
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## links: check links in published site
links:
	linkchecker -F text https://codebender.org/

## serve: serve generated HTML
serve:
	@python -m http.server -d docs
