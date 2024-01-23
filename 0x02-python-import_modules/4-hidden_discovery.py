#!/usr/bin/python3
import dis

def get_names_from_pyc(file_path):
    with open(file_path, 'rb') as file:
        magic_number = file.read(4)
        modification_time = file.read(4)
        code_object = compile(file.read(), '<string>', 'exec')

    names = [name for name in dir(code_object) if not name.startswith('__')]
    names.sort()

    return names

if __name__ == "__main__":
    file_path = "hidden_4.pyc"
    names = get_names_from_pyc(file_path)

    for name in names:
        print(name)
