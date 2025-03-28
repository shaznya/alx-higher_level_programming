#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    module_name = "hidden_4"
    module_path = "./hidden_4.pyc"

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    names = dir(hidden_4)

    filtered_names = sorted(name for name in names if not name.startswith("__"))

    for name in filtered_names:
        print(name)
