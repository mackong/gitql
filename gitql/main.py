#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import readline
import atexit
import argparse

from termcolor import cprint

from . import __version__, show_all_tables
from .errors import GitQLError
from .lexer import Lexer
from .parser import Parser
from .gitql import GitQL

# Borrow from Lib/timeit.py
if sys.platform == "win32":
    # On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time()
    default_timer = time.time

if sys.version_info < (3, ):
    input = raw_input
else:
    input = input


def init_readline():
    hisfile = os.path.join(os.path.expanduser('~'), '.gitql_hist')
    try:
        readline.read_history_file(hisfile)
        readline.set_history_length(1000)
    except IOError:
        pass

    atexit.register(readline.write_history_file, hisfile)

    readline.parse_and_bind("tab: complete")


def print_footer(nrows, ellapse):
    # TODO make ellapse more accurate.
    fmt = '{} row{} in set ({:.2f} sec)\n'
    s = fmt.format(nrows, 's' if nrows > 1 else '', ellapse)
    cprint(s, attrs=['bold'])


def print_table(header, rows):
    import prettytable
    pt = prettytable.PrettyTable(header, hrules=prettytable.ALL)
    pt.align = 'l'
    for row in rows:
        pt.add_row(row)
    print(pt)


def print_json(header, rows):
    # TODO
    pass


def run(query, out_type, path):
    t0 = default_timer()

    try:
        lexer = Lexer(query)
        parser = Parser(lexer)
        ql = GitQL(parser, path)
        header, rows = ql.run()
    except GitQLError as e:
        print(e)
        return

    ellapse = default_timer() - t0
    if out_type == 'table':
        print_table(header, rows)
    elif out_type == 'json':
        print_json(header, rows)

    print_footer(len(rows), ellapse)


def run_interactive(args):
    init_readline()

    while 1:
        try:
            query = input('gitql> ')
        except EOFError:
            break

        query = query.strip()

        if not query:
            continue

        if query.lower() in ('exit', 'quit'):
            break

        run(query, args['type'], args['path'])


def get_parser():
    ap = argparse.ArgumentParser(
        prog='gitql', description='Git query language')
    ap.add_argument(
        'sql', metavar='SQL', type=str, nargs='?', help='A query to run')
    ap.add_argument(
        '-i',
        '--interactive',
        action='store_true',
        help='Enter to interactive mode')
    ap.add_argument(
        '-p',
        '--path',
        default='.',
        help='The path to run gitql (default ".")')
    ap.add_argument(
        '-s', '--show-tables', action='store_true', help='Show all tables')
    ap.add_argument(
        '-t',
        '--type',
        choices=['table', 'json'],
        default='table',
        help='The output type format (default "table")')
    ap.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s ' + __version__,
        help='Show the version of gitql')
    return ap


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['show_tables']:
        show_all_tables()
        return

    if args['interactive']:
        run_interactive(args)
    elif not args['sql']:
        parser.print_help()
        return
    else:
        run(args['sql'], args['type'], args['path'])


if __name__ == '__main__':
    main()
