#!/usr/bin/python3
import dis
import hidden_4

def print_function_names(module):

    code_objects = [item for item in module.__dict__.values() if callable(item)]

    for code_object in code_objects:
        if callable(code_object) and not code_object.__name__.startswith("__"):
            print(code_object.__name__)

print_function_names(hidden_4)
