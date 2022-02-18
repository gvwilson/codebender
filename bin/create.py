#!/usr/bin/env python

"""Create final pages from templates."""


import argparse
import ibis
import os
import sys


def main():
    """Main driver."""
    options = parse_args()
    for filename in options.render:
        render(options, filename)
    for filename in options.copy:
        copy(options, filename)


def render(options, src):
    pass


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--clean", type=bool, default=True, help="Clean output.")
    parser.add_argument("--copy", nargs="+", help="Files to copy.")
    parser.add_argument("--outdir", type=str, help="Output directory.")
    parser.add_argument("--render", nargs="+", help="Files to render.")
    parser.add_argument("--templates", type=str, help="Template directory")
    return parser.parse_args(sys.argv[1:])


def render(options, src):
    pass


if __name__ == "__main__":
    main()
