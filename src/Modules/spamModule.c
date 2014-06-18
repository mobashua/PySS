/*	The objective is to call :
		>>> import spam
		>>> status = spam.system("ls -l")
*/

// The Python API, that provides access to most aspects
// of the Python run-time system
#include <Python.h>

static PyObject *
spam_system(PyObject *self, PyObject *args){
	const char *command;
	int sts;
	
	if(!PyArg_ParseTuple(args, "s", &command)){
		return NULL;
	}
	sts = system(command)
	return Py_BuildValue("i", sts);
}
