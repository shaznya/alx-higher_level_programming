#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, item->ob_type->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: A PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    if (size > 10)
        size = 10;

    printf("  first %zd bytes: ", size + 1);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}
