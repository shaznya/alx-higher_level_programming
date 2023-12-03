#!/usr/bin/python3
import importlib.util

def print_module_names(file_path):
    module_name = "module_name"  # Choose a name for the temporary module

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith('__')]

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    file_path = "hidden_4.pyc"
    print_module_names(file_path)
