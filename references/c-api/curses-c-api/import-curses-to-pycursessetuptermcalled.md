# curses c api C API: `import_curses()`, `PyCurses_API_pointers`, `PyCursesWindow_Type`, `PyCursesWindow_Check()`, `PyCursesSetupTermCalled`

## Curses C API

### Curses C API

[`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) offers extension modules a compact C surface. To use it you pull in the `py_curses.h` header file (which `Python.h` does not bring in on its own) and call `import_curses()`, typically inside your module's initialisation routine, so that `PyCurses_API` gets filled in.

Warning

Subinterpreters work with neither this C API nor the all-Python [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module.

 import_curses()

Bring in the curses C API. You can invoke this macro without appending a semi-colon.

On success, populate the `PyCurses_API` pointer.

When it fails, `PyCurses_API` is left as NULL and an exception is raised. Detecting that error is up to the caller, who tests it through [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred):

```c
import_curses();  // semi-colon is optional but recommended
if (PyErr_Occurred()) { /* cleanup */ }

```

 void **PyCurses_API

A heap-allocated object that carries the curses C API. You can reach this variable only after `import_curses` has succeeded.

`PyCurses_API[0]` corresponds to `PyCursesWindow_Type`.

`PyCurses_API[1]`, `PyCurses_API[2]`, and `PyCurses_API[3]` are pointers to predicate functions of type `int (*)(void)`.

When called, these predicates return whether [`curses.setupterm()`](https://docs.python.org/3.14/library/curses.html#curses.setupterm), [`curses.initscr()`](https://docs.python.org/3.14/library/curses.html#curses.initscr), and [`curses.start_color()`](https://docs.python.org/3.14/library/curses.html#curses.start_color) have been called respectively.

See also the convenience macros `PyCursesSetupTermCalled`, `PyCursesInitialised`, and `PyCursesInitialisedColor`.

Note

How many entries this structure holds may shift over time. To find out whether additional fields exist, lean on `PyCurses_API_pointers`.

 PyCurses_API_pointers

How many reachable fields (`4`) `PyCurses_API` currently exposes. Each time fresh fields appear, this count goes up.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCursesWindow_Type

The [heap type](https://docs.python.org/3.14/c-api/typeobj.html#heap-types) corresponding to [`curses.window`](https://docs.python.org/3.14/library/curses.html#curses.window).

 int PyCursesWindow_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Return true if *op* is a [`curses.window`](https://docs.python.org/3.14/library/curses.html#curses.window) instance, false otherwise.

The macros listed next are shorthands that expand to C statements. Because of that, you write them as `macro;` or `macro` alone, never in the `macro()` or `macro();` forms.

 PyCursesSetupTermCalled

Macro checking if [`curses.setupterm()`](https://docs.python.org/3.14/library/curses.html#curses.setupterm) has been called.

The macro expansion is roughly equivalent to:

```c
{
    typedef int (*predicate_t)(void);
    predicate_t was_setupterm_called = (predicate_t)PyCurses_API[1];
    if (!was_setupterm_called()) {
        return NULL;
    }
}

```

[Subject index](INDEX.md) · [Previous source contract](../coroutine-objects/pycoroobject-to-pycoro-new.md) · [Following source contract](pycursesinitialised-to-pycursesinitialisedcolor.md)
