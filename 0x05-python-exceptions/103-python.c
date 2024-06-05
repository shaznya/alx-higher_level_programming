#!/usr/bin/python3
#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    if (size > 10)
        size = 10;

    printf("  first %ld bytes: ", size);
    str = PyBytes_AsString(p);
    for (i = 0; i < size; i++) {
        printf("%02hhx", str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    PyFloatObject *f = (PyFloatObject *)p;

    if (!PyFloat_Check(f)) {
        printf("[ERROR] Invalid PyFloatObject\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", f->ob_fval);
}

int main(void) {
    Py_Initialize();
    PyObject *list = PyList_New(3);
    PyList_SetItem(list, 0, PyLong_FromLong(1));
    PyList_SetItem(list, 1, PyUnicode_FromString("hello"));
    PyList_SetItem(list, 2, PyFloat_FromDouble(3.14));
    print_python_list(list);

    PyObject *bytes = PyBytes_FromString("This is a bytes object");
    print_python_bytes(bytes);

    PyObject *f = PyFloat_FromDouble(3.14159265359);
    print_python_float(f);

    Py_DECREF(list);
    Py_DECREF(bytes);
    Py_DECREF(f);

    Py_Finalize();
    return 0;
}
