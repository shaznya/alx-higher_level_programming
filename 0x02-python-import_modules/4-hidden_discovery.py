#!/usr/bin/python3
import marshal

def extract_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as file:
        magic = file.read(4)
        if magic != b'\x03\xf3\r\n':
            raise ValueError("Not a valid Python 3.8 bytecode file.")

        file.read(8)

        names = set()
        try:
            while True:
                try:
                    code = marshal.load(file)
                except EOFError:
                    break

                if isinstance(code, type((lambda: 0).__code__)):
                    names.update(code.co_names)
        except Exception as e:
            print(f"An error occurred: {e}")

    filtered_names = sorted(name for name in names if not name.startswith("__"))
    for name in filtered_names:
        print(name)

if __name__ == "__main__":
    extract_names_from_pyc("hidden_4.pyc")
