#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t size, i;
Py_ssize_t allocated;
PyObject *item;

size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
