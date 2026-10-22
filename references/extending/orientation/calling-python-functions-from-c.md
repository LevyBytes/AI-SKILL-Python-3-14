# Calling Python Functions from C

### 1.6. Calling Python Functions from C

Up to here we have focused on making C functions callable from Python. The opposite direction proves useful as well: calling Python functions from C. This comes up especially for libraries that support so-called “callback” functions. When a C interface relies on callbacks, the matching Python interface frequently has to offer a callback mechanism to the Python programmer; implementing it will mean calling the Python callback functions from a C callback. Still other uses can be imagined.

[Subject index](INDEX.md) · [Previous source section](compilation-and-linkage.md) · [Required Calling Python functions from C continuation](calling-python-functions-from-c-and-pyerr-clear.md)
