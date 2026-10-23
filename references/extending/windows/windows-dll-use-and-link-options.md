# Using DLLs in Practice - PyArg_ParseTuple, Py_NO_LINK_LIB, PyObject

### 5.3. Using DLLs in Practice

The Windows build of Python is compiled with Microsoft Visual C++, and whether any other compiler succeeds is hit or miss. Everything that follows in this section assumes MSVC++.

As you build DLLs on Windows, there are a couple of distinct ways to draw on the CPython library:

1.

Out of the box, pulling in `PC/pyconfig.h` either on its own or through `Python.h` sets off an automatic, configuration-aware link against the library. Which library the header picks depends on the build: `pythonXY_d.lib` for Debug, `pythonXY.lib` for Release, and `pythonX.lib` for a Release that turns on the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable-application-binary-interface).

Say you want to produce a pair of DLLs — spam plus ni, where ni calls C functions living in spam — the commands below would do it:

```c
cl /LD /I/python/include spam.c
cl /LD /I/python/include ni.c spam.lib

```

That opening command emitted a trio of files: `spam.obj`, `spam.dll` and `spam.lib`. Although `Spam.dll` carries none of the Python functions itself (for instance [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple)), it can still locate the Python code by way of the implicitly linked `pythonXY.lib`.

Running the second command produced `ni.dll` (plus `.obj` and `.lib`), and that module is able to track down the functions it needs both from spam and from the Python executable.

2.

By hand: define the `Py_NO_LINK_LIB` macro ahead of the point where you include `Python.h`. In that case it falls to you to supply `pythonXY.lib` to the linker yourself.

Once again, to turn out the two DLLs spam and ni — with ni relying on C functions that reside in spam — you might run the following:

```c
cl /LD /DPy_NO_LINK_LIB /I/python/include spam.c ../libs/pythonXY.lib
cl /LD /DPy_NO_LINK_LIB /I/python/include ni.c spam.lib ../libs/pythonXY.lib

```

Here too the first command yielded three outputs: `spam.obj`, `spam.dll` and `spam.lib`. Even though `Spam.dll` packs no Python functions of its own (take [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) as an example), it nonetheless manages to reach the Python code through `pythonXY.lib`.

As before, the second command turned out `ni.dll` (along with `.obj` and `.lib`), a module that can resolve the functions it requires from spam as well as from the Python executable.

The lookup table does not receive every identifier automatically. For any other module — Python included — to be capable of seeing your identifiers, you must annotate them with `_declspec(dllexport)`, the way it appears in `void _declspec(dllexport) initspam(void)` or in `PyObject _declspec(dllexport) *NiGetSpamData(void)`.

Developer Studio tends to pull in a heap of import libraries you have no actual use for, inflating your executable by roughly 100K. Clearing them out is a matter of opening the Project Settings dialog, going to the Link tab, and choosing *ignore default libraries*. Then drop the appropriate `msvcrt*xx*.lib` into the libraries list.

[Subject index](INDEX.md) · [Previous source section](differences-between-unix-and-windows-py-no-link-lib.md)
