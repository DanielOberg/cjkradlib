import re

try:
    from importlib.resources import read_text as import_text
except ImportError:
    from importlib_resources import read_text as import_text


class Decompose:
    def __init__(self):
        self.entries = dict()
        self.super_entries = dict()

        for row in import_text('cjkradlib.data', 'cjk-decomp.txt').strip().split('\n'):
            entry, _, components = re.match('(.+):(.+)\((.*)\)', row).groups()
            comp_list = components.split(',')
            self.entries[entry] = comp_list
            for comp in comp_list:
                self.super_entries.setdefault(comp, []).append(entry)

    def get_sub(self, char):
        return self.entries.get(char, [])

    def get_super(self, char):
        return self.super_entries.get(char, [])
