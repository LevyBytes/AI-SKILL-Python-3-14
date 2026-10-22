# Isolated Module Objects

### Isolated Module Objects

The central idea to hold onto while building an extension module is that one shared library can yield several module objects. As an illustration:

```pycon
>>> import sys
>>> import binascii
>>> old_binascii = binascii
>>> del sys.modules['binascii']
>>> import binascii  # create a new module object
>>> old_binascii == binascii
False

```

As a guideline, the two modules ought to stay fully separate. Every object and piece of state tied to the module belongs inside the module object — never shared with the other module objects, and released once the module object is deallocated. Because this is merely a guideline, exceptions can occur (consult Managing Global State), though they call for extra deliberation and care over edge cases.

Even though certain modules might get by with looser constraints, isolated modules make it simpler to set definite expectations and guidance that hold across many different use cases.

[Subject index](INDEX.md) · [Previous source context](enter-per-module-state.md) · [Following source context](surprising-edge-cases.md)
