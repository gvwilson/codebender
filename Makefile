JEKYLL=jekyll
SITE=./_site

BIB2HTML=./bin/bib2html.py
BIB_SRC=./codebender.bib
BIB_DST=./_includes/bibliography.html

GLOSS_SRC=./_data/glossary.yml

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*.html)
LAYOUTS=$(wildcard _layouts/*.html)
STATIC=$(wildcard static/*.*)
SUPPORT=${BIB_DST}
SOURCE=index.html $(wildcard *.md) $(wildcard */index.html) $(wildcard */index.md)

LATEX=pdflatex
BIBTEX=bibtex
STEM=mrsp

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build: ${SUPPORT}
	${JEKYLL} build

## serve: build site and run server
serve: ${SUPPORT}
	${JEKYLL} serve

## bib: re-create HTML bibliography of reviewed articles
bib: ${BIB_DST}

## check: check integrity
check:
	@bin/check.py --bib ${BIB_SRC} --gloss ${GLOSS_SRC} --content ${SOURCE}

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@rm -rf $$(cat .gitignore) ${SITE}

## pdf : re-generate PDF
pdf :
	${LATEX} ${STEM}
	${BIBTEX} ${STEM}
	${LATEX} ${STEM}
	${LATEX} ${STEM}

## count: count the number of slides in each lecture
count:
	@bin/count-slides.py _config.yml

## links: check integrity of links (assumes a server is running locally)
links:
	linkchecker "http://localhost:4000"

## spelling: check spelling of generated site
spelling:
	@cat $$(find _site -name '*.html') | aspell -H list | sort | uniq | bin/setdiff.py - _data/spelling.txt

# ---

# Make the bibliography file.
${BIB_DST}: ${BIB_SRC} ${BIB2HTML}
	${BIB2HTML} --action bib2md --no_abstract < $< >  $@
