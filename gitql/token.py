#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from typing import Any


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class TokenType(AutoNumber):
    T_SELECT = ()
    T_FROM = ()
    T_WHERE = ()
    T_ORDER = ()
    T_BY = ()
    T_LIMIT = ()
    T_OFFSET = ()
    T_IN = ()
    T_DESC = ()
    T_ASC = ()
    T_AND = ()
    T_OR = ()
    T_NOT = ()
    T_IDENTIFIER = ()
    T_NUMBER = ()
    T_STRING = ()
    T_ASTERISK = ()  # *
    T_COMMA = ()  # ,
    T_SEMICOLON = ()  # ;
    T_LPARAN = ()  # (
    T_RPARAN = ()  # )
    T_EQ = ()  # =
    T_GT = ()  # >
    T_GTE = ()  # >=
    T_LT = ()  # <
    T_LTE = ()  # <=
    T_NEQ = ()  # !=
    T_EOF = ()


class Token:
    def __init__(self, token_type: TokenType, value: Any):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return 'Token({!r}, {!r})'.format(self.token_type.name, self.value)
