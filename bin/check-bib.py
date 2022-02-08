#!/usr/bin/env python

import bibtexparser
import re
import sys

with open(sys.argv[1], "r") as reader:
    entries = bibtexparser.load(reader).entries
    known = {x["ID"] for x in entries}

pat = re.compile(r'<cite>(.+?)</cite>')
used = set()
for filename in sys.argv[2:]:
    with open(filename, "r") as reader:
        text = reader.read()
        for match in pat.finditer(text):
            used |= {x.strip() for x in match.group(1).split(",")}

print("missing", ", ".join(used - known))
print("unused", ", ".join(known - used))
