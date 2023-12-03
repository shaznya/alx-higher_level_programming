#!/usr/bin/python3
import dis
import hidden_4

def print_names_from_pyc(module):
    # Extract code objects from the module
    code_objects = [item for item in module.__dict__.values() if callable(item)]

    names = []
    for code_object in code_objects:
        if callable(code_object) and not code_object.__name__.startswith("__"):
            names.append(code_object.__name__)
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_names_from_pyc(hidden_4)
