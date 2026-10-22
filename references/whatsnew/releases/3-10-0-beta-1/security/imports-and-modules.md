# Python 3.10.0 beta 1 / security / imports and modules

[bpo-43472](https://bugs.python.org/issue?@action=redirect&bpo=43472): Guarantees that interpreter-level audit hooks are handed the `cpython.PyInterpreterState_New` event whenever invocation happens by way of the `_xxsubinterpreters` module.

[bpo-43362](https://bugs.python.org/issue?@action=redirect&bpo=43362): Repair an invalid free within the _sha3 module. This bug entered in 3.10.0a1. Neither Python 3.9 nor earlier releases are affected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
