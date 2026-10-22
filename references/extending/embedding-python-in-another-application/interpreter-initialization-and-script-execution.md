# Embedding Python in Another Application — Py_Initialize, PyRun_SimpleString, PyRun_SimpleFile

## 1. Embedding Python in Another Application

### 1. Embedding Python in Another Application

Earlier chapters covered how you extend Python, namely by bolting a library of C functions onto it to broaden what Python can do. The reverse direction is open to you as well: you can enhance a C/C++ application by embedding Python within it. Embedding lets your application carry out some of its own work in Python instead of in C or C++. Plenty of purposes suit this; one such case lets users adapt the application to their own needs by penning a few Python scripts. You might also turn to it yourself wherever a given piece of functionality comes together more readily in Python.

There is a resemblance between embedding Python and extending it, though they are not identical. What sets them apart is that with extension the application's main program remains the Python interpreter, whereas with embedding the main program need bear no relation to Python at all — rather, certain portions of the application now and again call on the Python interpreter to run a bit of Python code.

So whenever you embed Python, the main program is yours to supply. Among that program's duties is bringing the Python interpreter to life. As a bare minimum, you must invoke the [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) function. Optional calls exist for handing command line arguments over to Python. From that point on, any part of the application may call the interpreter.

Several routes lead to the interpreter: you might hand a string of Python statements to [`PyRun_SimpleString()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_SimpleString), or pass a stdio file pointer plus a file name (used purely to identify it in error messages) to [`PyRun_SimpleFile()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_SimpleFile). Alternatively you can reach for the lower-level operations laid out in earlier chapters to build and work with Python objects.

See also

[Python/C API reference manual](https://docs.python.org/3.14/c-api/index.html#c-api-index)

This manual sets out the particulars of Python's C interface. You will find a great quantity of the information you need within it.

[Subject index](INDEX.md) · [Previous source section](../building-c-and-c-extensions/building-c-and-c-extensions-with-setuptools.md) · [Next source section](very-high-level-embedding-and-pyrun-simplefile.md)
