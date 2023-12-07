#!/usr/bin/python3
import importlib.util

def get_names_from_pyc(file_path):
    # Create a new module
    module_name = 'dummy_module'
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = [name for name in dir(module) if not name.startswith('__')]

    names.sort()

    return names

if __name__ == "__main__":
    pyc_file_path = 'hidden_4.pyc'
    names = get_names_from_pyc(pyc_file_path)
    for name in names:
        print(name)
