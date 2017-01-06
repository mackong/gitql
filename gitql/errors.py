#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored


class GitQLError(Exception):
    """Exceptions in gitql."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return '{}: {}'.format(colored('GitQLError', 'red'), self.message)
