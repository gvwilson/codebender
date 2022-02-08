#!/usr/bin/env python

'''Count the number of slides in each input file.'''

import os
import re
import sys
import yaml


BREAK = re.compile(r'^---$', re.MULTILINE)


def main():
    config = read_config(sys.argv[1])
    paths = make_paths(config)
    count(paths)


def read_config(filename):
    with open(filename, 'r') as reader:
        text = reader.read()
        return yaml.load(text, Loader=yaml.FullLoader)


def make_paths(config):
    return [os.path.join(entry['slug'], 'index.html')
            for entry in config['lessons']
            if 'title' in entry]


def count(paths):
    for path in paths:
        with open(path, 'r') as reader:
            text = reader.read()
            num = len(BREAK.findall(text)) - 2 # because of file header
            print(f'{num:2}: {path}')


if __name__ == '__main__':
    main()
