#!/usr/bin/env python

import sys
import util


def main():
    left = get_words(sys.argv[1])
    right = get_words(sys.argv[2])
    util.report('unknown words', left - right)
    util.report('unused spelling entries', right - left)


def get_words(filename):
    if filename == '-':
        return {x.strip() for x in sys.stdin.readlines()}
    with open(filename, 'r') as reader:
        return {x.strip() for x in reader.readlines()}


if __name__ == '__main__':
    main()
