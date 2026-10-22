# Background

### Background

The term *interpreter* refers to the surrounding context where Python code executes. It holds configuration (such as the import path) together with runtime state (such as the collection of imported modules).

Within a single process, Python can run several interpreters at once. Two scenarios deserve consideration — a user might run interpreters:

- one after another, across a number of [`Py_InitializeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeEx)/[`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) cycles, and

- side by side, driving ?sub-interpreters? through [`Py_NewInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_NewInterpreter)/[`Py_EndInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_EndInterpreter).

These scenarios — and any mix of the two — prove most valuable when Python is embedded inside a library. As a rule, libraries should avoid presuming things about whatever application calls them, including the presumption of a process-wide ?main Python interpreter?.

In the past, Python extension modules have handled this scenario poorly. A great many extension modules (and a handful of stdlib modules too) rely on *per-process* global state, simply because C `static` variables are so trivial to reach for. As a result, data meant to belong to one interpreter winds up shared among interpreters. Without care from the extension developer, it becomes trivially easy to create edge cases that crash once a module is loaded into more than one interpreter inside the same process.

Sadly, *per-interpreter* state is hard to pull off. Authors of extensions rarely keep several interpreters in view while building, and exercising the behavior remains awkward at present.

[Subject index](INDEX.md) · [Previous source context](who-should-read-this.md) · [Following source context](enter-per-module-state.md)
