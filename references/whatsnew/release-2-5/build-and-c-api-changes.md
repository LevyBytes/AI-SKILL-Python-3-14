# What's New in Python 2.5 / Build and C API Changes

### Build and C API Changes

Among the changes to Python's build process and to the C API are:

- The Python source tree moved from CVS over to Subversion, by way of an intricate migration that Martin von Löwis oversaw and executed without a flaw. That procedure took shape as [**PEP 347**](https://peps.python.org/pep-0347/).

- Coverity, a firm selling a source code analysis tool named Prevent, shared with the project the findings from running it against the Python source code. Roughly 60 bugs turned up in the analysis and were promptly fixed. A large share were refcounting issues, many of them in error-handling code. The statistics live at [https://scan.coverity.com](https://scan.coverity.com).

- [**PEP 353**](https://peps.python.org/pep-0353/) drove the biggest C API change, reworking the interpreter so that it relies on a [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) type definition in place of int. The earlier section PEP 353: Using ssize_t as the index type covers this change in detail.

- The bytecode compiler's design shifted substantially, dropping the old approach of emitting bytecode by walking the parse tree. The parse tree is now turned into an abstract syntax tree (or AST), and it is that abstract syntax tree which gets walked to emit the bytecode.

Python code can get hold of AST objects through the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in by passing `_ast.PyCF_ONLY_AST` as the *flags* parameter's value:

```python
from _ast import PyCF_ONLY_AST
ast = compile("""a=0
for i in range(10):
    a += i
""", "<string>", 'exec', PyCF_ONLY_AST)

assignment = ast.body[0]
for_loop = ast.body[1]

```

The AST code does not yet have any formal documentation, though [**PEP 339**](https://peps.python.org/pep-0339/) covers the design rationale. A good entry point for studying the implementation is the various AST node definitions found in `Parser/Python.asdl`. That file is consumed by a Python script that produces matching C structure declarations in `Include/Python-ast.h`. Two functions declared in `Include/pythonrun.h` — `PyParser_ASTFromString()` and `PyParser_ASTFromFile()` — accept Python source text and hand back the AST root describing what was parsed. From there, `PyAST_Compile()` converts that tree into a code object. To dig deeper, browse the sources directly and then bring your questions to python-dev.

Jeremy Hylton oversaw development of the AST code. Its implementation came from the following contributors: Brett Cannon, Nick Coghlan, John Ehresman, Grant Edwards, Kurt Kaiser, Neal Norwitz, Tim Peters, Armin Rigo, Neil Schemenauer — plus everyone who took part in several AST sprints held at gatherings like PyCon.

- A patch to obmalloc written by Evan Jones, originally presented during a talk at PyCon DC 2005, was merged in. In Python 2.4 small objects were placed in 256K arenas, yet those arenas were never released. After this patch, an arena gets freed once it becomes empty. As a practical consequence, on certain platforms a program that creates a large number of objects might see Python’s memory footprint actually shrink once those objects are deleted, returning that memory to the OS. (Evan Jones built this, with rework from Tim Peters.)

Keep in mind that, because of this, extension modules have to take greater care when they request memory. Python’s API exposes a variety of memory-allocation functions organized into families. For instance, [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc), [`PyMem_Realloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Realloc), and [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free) form one family that handles raw memory, whereas [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc), [`PyObject_Realloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Realloc), and [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) belong to a separate family intended for building Python objects.

In earlier releases every one of these families ultimately bottomed out in the platform’s `malloc()` and `free()` routines. That meant a mismatch — allocating through `PyMem` but releasing through `PyObject` — went unnoticed and caused no harm. Following 2.5’s obmalloc rework, the families behave distinctly and a mismatch will very likely crash with a segfault. Be sure to exercise your C extension modules thoroughly under Python 2.5.

- There is now a supported C API for the built-in set types. Use [`PySet_New()`](https://docs.python.org/3.14/c-api/set.html#c.PySet_New) and [`PyFrozenSet_New()`](https://docs.python.org/3.14/c-api/set.html#c.PyFrozenSet_New) to construct a fresh set, [`PySet_Add()`](https://docs.python.org/3.14/c-api/set.html#c.PySet_Add) and [`PySet_Discard()`](https://docs.python.org/3.14/c-api/set.html#c.PySet_Discard) to insert and delete members, plus [`PySet_Contains()`](https://docs.python.org/3.14/c-api/set.html#c.PySet_Contains) and [`PySet_Size()`](https://docs.python.org/3.14/c-api/set.html#c.PySet_Size) to inspect what the set currently holds. (Contributed by Raymond Hettinger.)

- From C code you can now query the precise revision of the running Python interpreter by invoking [`Py_GetBuildInfo()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetBuildInfo), which yields a build-description string of the form `"trunk:45355:45356M, Apr 13 2006, 07:42:19"`. (Contributed by Barry Warsaw.)

- A pair of fresh macros lets you flag C functions as confined to the current source file, enabling a quicker calling convention. [`Py_LOCAL`](https://docs.python.org/3.14/c-api/intro.html#c.Py_LOCAL) marks the function as returning a value of the given *type* while applying a fast-call qualifier. [`Py_LOCAL_INLINE`](https://docs.python.org/3.14/c-api/intro.html#c.Py_LOCAL_INLINE) behaves identically and additionally asks for the function to be inlined. When the macro `PY_LOCAL_AGGRESSIVE` is defined ahead of including `python.h`, the module gains a batch of more aggressive optimizations; benchmark the outcome to confirm whether they genuinely speed up your code. (Contributed by Fredrik Lundh at the NeedForSpeed sprint.)

- `PyErr_NewException(name, base, dict)` will now also take a tuple of base classes for its *base* argument. (Contributed by Georg Brandl.)

- The warning-emitting function `PyErr_Warn()` is now deprecated, replaced by `PyErr_WarnEx(category, message, stacklevel)`, which lets you state how many stack frames lie between this call and its caller. A *stacklevel* value of 1 refers to the function that invokes [`PyErr_WarnEx()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WarnEx), 2 points one level higher, and so on. (Added by Neal Norwitz.)

- While CPython’s interpreter remains a C program, its sources can at last be built using a C++ compiler with no errors reported. (Implemented by Anthony Baxter, Martin von Löwis, Skip Montanaro.)

- The `PyRange_New()` function has been dropped. It was undocumented, unused throughout the core, and performed perilously loose error checking. On the off chance that some extension of yours relied on it, a substitute along these lines will serve:

```python
range = PyObject_CallFunction((PyObject*) &PyRange_Type, "lll",
                              start, stop, step);

```

[Subject index](INDEX.md) · [Previous source section](the-wsgiref-package.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Next source section](port-specific-changes.md)
