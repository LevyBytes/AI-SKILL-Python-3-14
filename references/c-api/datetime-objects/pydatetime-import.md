# datetime objects C API: `PyDateTime_IMPORT()`

# Datetime, Descriptor

## Overview

Covers: DateTime Objects; Descriptor Objects.

## DateTime Objects

### DateTime Objects

The [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module furnishes an assortment of date and time objects. Ahead of calling any of the functions here, your source has to include the header file `datetime.h` (be aware that `Python.h` does not pull it in for you), and you must invoke the macro `PyDateTime_IMPORT` — typically from within the module initialisation function. That macro stashes a pointer to a C structure inside a static variable, `PyDateTimeAPI`, which the macros below then rely on.

 PyDateTime_IMPORT()

Import the datetime C API.

When it works, the `PyDateTimeAPI` pointer gets filled in. When it doesn't, `PyDateTimeAPI` is left as `NULL` and an exception is raised. It falls to the caller to detect any error through [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred):

```c
PyDateTime_IMPORT;
if (PyErr_Occurred()) { /* cleanup */ }

```

Warning

This is not compatible with subinterpreters.

[Subject index](INDEX.md) · [Following source contract](pydatetime-capi-to-pydatetimeapi.md)
