#!/usr/bin/env python

'''Check consistency.'''

import argparse
from collections import Counter
import re
import util


RAW = re.compile(r'{%\s+raw\s+%}.+?{%\s+endraw\s+%}')
CITE = re.compile(r'<cite>(.+?)</cite>')
GLOSS_EXTERNAL = re.compile(r'\]\(g#(.+?)\)')
GLOSS_INTERNAL = re.compile(r']\(#(.+?)\)')


def main():
    options = get_options()
    files = load_files(options.content)

    bib = util.get_bib(*options.bib)
    check_bib(bib)
    check_cites(bib, files)

    gloss = util.get_gloss(options.gloss)
    check_gloss(gloss)
    check_defs(gloss, files)


def check_bib(bib):
    temp = Counter([entry['ID'] for entry in bib])
    temp = [key for key in temp if temp[key] > 1]
    util.report('duplicate bibliography keys', temp)


def check_cites(bib, files):
    unknown = {}
    known = {entry['ID'] for entry in bib}
    for filename in files:
        for match in CITE.finditer(files[filename]):
            keys = [k.strip() for k in match.group(1).split(',')]
            for k in keys:
                if k not in known:
                    unknown[k] = filename
    unknown = [f'{key}: {unknown[key]}' for key in unknown]
    util.report('unknown bibliography keys', unknown)


def check_gloss(gloss):
    util.report('glossary entries out of order', gloss_disordered(gloss))
    util.report('duplicate glossary keys or terms', gloss_duplicate(gloss))


def check_defs(gloss, files):
    defs = {entry['key'] for entry in gloss}
    refs = get_gloss_refs(files) | get_gloss_internal(gloss)
    util.report('unknown glossary keys', refs - defs)
    util.report('unused glossary keys', defs - refs)


def get_gloss_refs(files):
    result = set()
    for filename in files:
        for match in GLOSS_EXTERNAL.finditer(files[filename]):
            result.add(match.group(1))
    return result


def get_gloss_internal(gloss):
    result = set()
    for entry in gloss:
        if 'ref' in entry:
            result |= set(entry['ref'])
        for match in GLOSS_INTERNAL.finditer(entry['def']):
            result.add(match.group(1))
    return result


def gloss_disordered(gloss):
    result = []
    prev = None
    for entry in gloss:
        curr = entry['term'].lower()
        if (prev is not None) and (prev > curr):
            result.append(curr)
        prev = curr
    return result


def gloss_duplicate(gloss):
    temp = Counter([entry['key'] for entry in gloss])
    temp = [key for key in temp if temp[key] > 1]
    util.report('duplicate glossary keys', temp)


def load_files(filenames):
    result = {}
    for fn in filenames:
        with open(fn, 'r') as reader:
            result[fn] = RAW.sub('', reader.read())
    return result


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bib', nargs='+', help='specify bibliography file(s)')
    parser.add_argument('--gloss', help='specify glossary file')
    parser.add_argument('--content', nargs='+', help='specify content file(s)')
    return parser.parse_args()


if __name__ == '__main__':
    main()
