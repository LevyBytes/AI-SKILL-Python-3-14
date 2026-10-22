# PYTHONHASHSEED

PYTHONHASHSEED

When this variable is absent or set to `random`, a random value seeds the hashes of str and bytes objects.

When `PYTHONHASHSEED` is set to an integer value, it serves as a fixed seed for producing the hash() of the types affected by hash randomization.

The point is to permit reproducible hashing, for example for the interpreter's own selftests, or to let a cluster of python processes agree on hash values.

The integer must be a decimal number within the range [0,4294967295]. Giving the value 0 will switch hash randomization off.

Added in version 3.2.3.

[Subject index](INDEX.md) · [Previous source section](pythonpycacheprefix.md) · [Following source section](pythonintmaxstrdigits.md)
