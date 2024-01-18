#!/usr/bin/python3
import marshal

def print_module_names(file_path):
    with open(file_path, 'rb') as f:
        code = marshal.load(f)

    module_names = [name for name in code.co_names if not name.startswith('__')]
    module_names.sort()

    for name in module_names:
        print(name)
        print_module_names('hidden_4.pyc')
