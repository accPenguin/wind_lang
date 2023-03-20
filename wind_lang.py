import re


class GPTLangInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
