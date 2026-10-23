# Providing a C API for an Extension Module - PyCapsule_New, PyCapsule_Import, PySpam_System, PyObject, PyArg_ParseTuple, PyLong_FromLong, Py_mod_exec

### 1.12. Providing a C API for an Extension Module

Plenty of extension modules merely contribute fresh functions and types for Python to call, yet on occasion one extension module's code proves handy to another. Picture an extension module that defines a type “collection” behaving like unordered lists. In the same way the built-in Python list type carries a C API letting extension modules build and operate on lists, this new collection type ought to expose a family of C functions other extension modules can drive directly.

On the surface this looks trivial: simply author the functions (leaving off the `static` declaration, naturally), supply a suitable header file, and write up the C API. And it really would work were every extension module forever linked statically into the Python interpreter. Once modules act as shared libraries, though, the symbols one module defines might stay invisible to another. How visibility behaves hinges on the operating system; certain ones give the Python interpreter and all extension modules a single global namespace (Windows being one), others demand an explicit roster of imported symbols when a module links (AIX, for instance), and still others present a menu of strategies (most Unices). Even with symbols globally visible, the module holding the functions you mean to invoke may not be loaded yet!

Portability accordingly forbids taking anything for granted about symbol visibility. The upshot is that every symbol within an extension module should bear the `static` declaration, the module's initialization function aside, so as to dodge name collisions with other extension modules (a topic the section The Module's Method Table and Initialization Function covers). It also means symbols that *should* reach other extension modules have to be exposed by some other route.

For shuttling C-level information (pointers) between one extension module and the next, Python offers a dedicated facility: Capsules. A Capsule is a Python data type that holds a pointer (void*). You may only build and read Capsules through their C API, but otherwise they travel around just like any Python object. Notably, you can bind one to a name inside an extension module's namespace. Another extension module is then able to import that module, fetch the value under this name, and pull the pointer out of the Capsule.

Capsules lend themselves to exporting an extension module's C API in numerous fashions. You might hand each function its own Capsule, or gather all the C API pointers into an array and advertise that array's address through a single Capsule. Furthermore, the chores of stashing and recovering the pointers can be split up across the providing module and its client modules in assorted ways.

No matter which approach you adopt, naming your Capsules correctly matters. [`PyCapsule_New()`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule_New) accepts a name parameter (const char*); although a `NULL` name is allowed, we urge you in the strongest terms to give one. Capsules with proper names afford a measure of runtime type-safety, whereas two unnamed Capsules simply cannot be told apart by any workable means.

Specifically, any Capsule that surfaces a C API ought to carry a name shaped by the following convention:

```c
modulename.attributename

```

The helper function [`PyCapsule_Import()`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule_Import) streamlines loading a C API delivered through a Capsule, provided the Capsule's name obeys this convention. That guarantee leaves C API users quite confident the Capsule they pull in really holds the right C API.

The example coming up shows a scheme that loads most of the work onto whoever writes the exporting module, a sensible trade for library modules in heavy use. It keeps every C API pointer (a lone one here!) in an array of void pointers that serves as a Capsule's value. That module's matching header file supplies a macro handling the import of the module and the recovery of its C API pointers; a client module need only fire this macro ahead of touching the C API.

For the exporting module we adapt the `spam` module taken from the section A Simple Example. Rather than invoking the C library function `system()` straight away, the `spam.system()` function defers to a `PySpam_System()` function, which in any real setting would naturally do something fancier (prepending “spam” to every command, perhaps). That `PySpam_System()` function is exported to other extension modules as well.

The `PySpam_System()` function is an ordinary C function, marked `static` just as the rest are:

```c
static int
PySpam_System(const char *command)
{
    return system(command);
}

```

Only a minor tweak is applied to the `spam_system()` function:

```c
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = PySpam_System(command);
    return PyLong_FromLong(sts);
}

```

Near the top of the module, immediately following this line

```c
#include <Python.h>

```

two more lines must be added:

```c
#define SPAM_MODULE
#include "spammodule.h"

```

That `#define` signals to the header file that it is being pulled into the exporting module instead of a client module. Lastly, the module's [`mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function has to handle setting up the C API pointer array:

[Subject index](INDEX.md) · [Previous source section](writing-extensions-in-c.md) · [Next source section](capsule-api-pointer-initialization.md)
