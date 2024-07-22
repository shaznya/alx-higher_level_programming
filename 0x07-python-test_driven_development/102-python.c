#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }
    
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    
    const char *type;
    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        type = "compact ascii";
    } else if (PyUnicode_IS_COMPACT(p)) {
        type = "compact unicode object";
    } else {
        type = "unicode object";
    }
    PyObject *str = PyUnicode_AsUTF8String(p);
    if (str == NULL) {
        printf("[ERROR] Failed to convert string\n");
        return;
    }
    char *value = PyBytes_AS_STRING(str);

    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);

    Py_XDECREF(str);
}
