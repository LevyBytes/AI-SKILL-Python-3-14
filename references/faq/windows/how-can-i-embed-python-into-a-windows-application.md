# How can I embed Python into a Windows application?

### How can I embed Python into a Windows application?

Here is a summary of what embedding the Python interpreter inside a Windows app involves:

1.

Do **not** compile Python straight into your .exe file. Under Windows, Python has to take the form of a DLL so it can manage importing modules that are themselves DLL's. (Here is the first crucial undocumented fact.) Link instead to `python*NN*.dll`, which usually lives in `C:\Windows\System`. The `*NN*` stands for the Python version, a figure like “33” for Python 3.3.

Two distinct routes exist for linking to Python. Load-time linking amounts to linking against `python*NN*.lib`, whereas run-time linking amounts to linking against `python*NN*.dll`. (As a general aside: `python*NN*.lib` is the so-called “import lib” that goes with `python*NN*.dll`, and all it does is define symbols for the linker.)

Run-time linking makes the link options far simpler, with the whole thing taking place at run time. Your code is required to load `python*NN*.dll` by way of the Windows `LoadLibraryEx()` routine. It must likewise reach the access routines and data inside `python*NN*.dll` (in other words, Python's C API's) through pointers fetched via the Windows `GetProcAddress()` routine. Macros can render the handling of these pointers invisible to whatever C code calls into Python's C API.

2.

With SWIG in the mix, building a Python “extension module” that surfaces the app's data and methods to Python becomes simple. SWIG takes care of nearly every grubby detail on your behalf. Out of it comes C code that you link *into* your .exe file (!) There is **no** need to produce a DLL file, which makes linking simpler still.

3.

SWIG produces an init function (a C function) whose name hinges on the extension module's name. Say the module is named leo; then the init function bears the name initleo(). Should you adopt SWIG shadow classes, which you ought to, the init function is named initleoc() instead. That one sets up a largely hidden helper class that the shadow class relies on.

What makes it possible to link the step 2 C code into your .exe file is that invoking the initialization function amounts to importing the module into Python! (Here is the second crucial undocumented fact.)

4.

Put briefly, the code below serves to initialize the Python interpreter together with your extension module.

```c
#include <Python.h>
...
Py_Initialize();  // Initialize Python.
initmyAppc();  // Initialize (import) the helper class.
PyRun_SimpleString("import myApp");  // Import the shadow class.

```

5.

Python's C API carries two problems that come to light once you employ a compiler other than MSVC, the very compiler that built pythonNN.dll.

Problem 1: Those so-called “Very High Level” functions accepting `FILE *` arguments break down in a multi-compiler environment, since what a `struct FILE` means varies from one compiler to the next. Viewed from the implementation side, these are actually very low level functions.

Problem 2: When SWIG builds wrappers around void functions, the code it emits is:

```c
Py_INCREF(Py_None);
_resultobj = Py_None;
return _resultobj;

```

Unfortunately, Py_None is a macro expanding into a reference to an intricate data structure, _Py_NoneStruct, that lives inside pythonNN.dll. Here too, the code falls apart in a mult-compiler environment. Swap such code out for:

```c
return Py_BuildValue("");

```

SWIG's `%typemap` command might conceivably automate that change, but I have never managed to make it function (I am a total SWIG newbie).

6.

Leaning on a Python shell script to raise a Python interpreter window from within your Windows app is unwise, because the window you get stands apart from your app's windowing system. You (or the wxPythonWindow class) ought to spin up a “native” interpreter window instead. Hooking that window up to the Python interpreter is straightforward. Python's i/o can be redirected toward _any_ object that handles read and write, so the only thing you require is a Python object (declared in your extension module) furnishing read() and write() methods.

[Subject index](INDEX.md)
