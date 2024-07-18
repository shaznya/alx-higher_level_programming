#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    // Check if p is a string object
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Invalid String Object\n");
        return;
    }

    // Extract information from the PyUnicodeObject
    PyUnicodeObject *unicode = (PyUnicodeObject *)p;
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *str = PyUnicode_AsUTF8(p);

    // Print Python string information
    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  length: %ld\n", length);
    printf("  value: %s\n", str);
}
