#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 *print_python_list_info - Prints basic info about Python lists.
 *@p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject * obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject*) p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		if (obj == NULL)
		{
			printf("Failed to retrieve element\n");
			continue;
		}

		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
