# 12.1. Introduction

## 12. Virtual Environments and Packages

### 12. Virtual Environments and Packages

### 12.1. Introduction

It's common for Python applications to depend on packages and modules that aren't shipped with the standard library. From time to time an application even needs one particular version of a library — perhaps because it relies on a fix that landed in that release, or because it was built against an interface from an older version of the library.

The upshot is that a single Python installation may be unable to satisfy what every application asks of it. Suppose application A wants version 1.0 of some module while application B wants version 2.0: those demands clash, and whichever of 1.0 or 2.0 you install, one of the two applications won't run.

What fixes this is to build a [virtual environment](https://docs.python.org/3.14/glossary.html#term-virtual-environment): a self-contained directory tree holding a Python installation tied to one particular Python version, together with a set of extra packages.

Separate applications can then draw on separate virtual environments. Going back to the clash from before, application A can keep its own virtual environment with version 1.0 in place, while application B keeps a second virtual environment holding version 2.0. And if application B later needs that library bumped to version 3.0, application A's environment stays untouched.

[Subject index](INDEX.md) · [Previous source section](../brief-tour-of-the-standard-library-part-ii/decimal-floating-point-arithmetic.md) · [Following source section](creating-virtual-environments.md)
