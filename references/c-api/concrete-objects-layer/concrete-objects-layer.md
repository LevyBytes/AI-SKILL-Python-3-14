# Concrete Objects Layer

# Concrete, Contextvars

## Overview

Covers: Concrete Objects Layer; Context Variables Objects.

## Concrete Objects Layer

### Concrete Objects Layer

Each function in this chapter targets a particular Python object type. Handing one an object of the wrong type is unwise; whenever a Python program gives you an object whose type you cannot vouch for, verify it before proceeding. To confirm that something is a dictionary, for instance, call [`PyDict_Check()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Check). The layout of this chapter mirrors the “family tree” of Python object types.

Warning

Although the routines here are careful about validating the type of every object handed to them, a good number neglect to guard against a `NULL` arriving in place of a real object. Letting `NULL` slip through can trigger memory access violations and abruptly kill the interpreter.

[Subject index](INDEX.md) · [Following source contract](fundamental-objects.md)
