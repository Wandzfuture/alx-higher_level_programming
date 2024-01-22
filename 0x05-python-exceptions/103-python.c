#include <Python.h>


/*Function to print Python list object */
void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	int i, length;

	if (!PyList_Check(p))
	{
		printf("Error: Input is not a Python list object\n");
		return;
	}

	list_obj = (PyListObject *) p;
	length = list_obj->ob_base.ob_size;

	printf("Python list object: %p\n", p);
	printf("List size: %d\n", length);

	for (i = 0; i < length; i++)
	{
		printf("Item %d: %p\n", i, PyList_GetItem(list_obj, i));
	}
}

/*Function to print Python bytes object */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_obj;
	int i, length;
	char *bytes;

	if (!PyBytes_Check(p))
	{
		printf("Error: Input is not a Python bytes object\n");
		return;
	}

	bytes_obj = (PyBytesObject *) p;
	length = bytes_obj->ob_size;
	bytes = PyBytes_AS_STRING(bytes_obj);

	printf("Python bytes object: %p\n", p);
	printf("Bytes size: %d\n", length);
	printf("First 10 bytes: ");

	for (i = 0; i < 10 && i < length; i++)
	{
		printf("%02x ", bytes[i]);
	}

	printf("\n");
}

/*Function to print Python float object */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj;

	if (!PyFloat_Check(p))
	{
		printf("Error: Input is not a Python float object\n");
		return;
	}

	float_obj = (PyFloatObject *) p;

	printf("Python float object: %p\n", p);
	printf("Float value: %.9g\n", ((PyFloatObject*) p)->ob_fval);
}
