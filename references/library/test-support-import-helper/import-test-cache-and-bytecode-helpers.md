# test.support.import_helper: Import test caches and bytecode helpers

### `test.support.import_helper` — Utilities for import tests

Support geared toward import tests is offered by the `test.support.import_helper` module.

Added in version 3.10.

 test.support.import_helper.forget(*module_name*)

Drop the module called *module_name* out of `sys.modules` and erase whatever byte-compiled files belong to that module.

 test.support.import_helper.import_fresh_module(*name*, *fresh=()*, *blocked=()*, *deprecated=False*)

This routine brings in and hands back a brand-new copy of the named Python module, accomplished by clearing that module out of `sys.modules` ahead of the import. Be aware that, in contrast to `reload()`, the original module comes through this untouched.

*fresh* is an iterable naming further modules that likewise get cleared from the `sys.modules` cache before the import proceeds.

*blocked* is an iterable of module names that, throughout the import, are swapped for `None` in the module cache so that any attempt to import them yields [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError).

The named module, plus every module called out in the *fresh* and *blocked* parameters, is stashed before the import kicks off and then dropped back into `sys.modules` once the fresh import wraps up.

Should *deprecated* be `True`, deprecation notices for modules and packages are muted while this import runs.

When the named module cannot be brought in, this routine raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError).

Example use:

```python
# Get copies of the warnings module for testing without affecting the
# version being used by the rest of the test suite. One copy uses the
# C implementation, the other is forced to use the pure Python fallback
# implementation
py_warnings = import_fresh_module('warnings', blocked=['_warnings'])
c_warnings = import_fresh_module('warnings', fresh=['_warnings'])

```

Added in version 3.1.

 test.support.import_helper.import_module(*name*, *deprecated=False*, ***, *required_on=()*)

This routine brings in and hands back the named module. Departing from an ordinary import, it raises [`unittest.SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest) whenever the module proves impossible to import.

When *deprecated* is `True`, deprecation notices for modules and packages stay muted across this import. If a module is mandatory on one platform yet optional elsewhere, give *required_on* an iterable of platform prefixes, which get matched against [`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform).

Added in version 3.1.

 test.support.import_helper.modules_setup()

Hand back a duplicate of [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

 test.support.import_helper.modules_cleanup(*oldmodules*)

Clear out modules apart from *oldmodules* and `encodings`, which keeps the internal cache intact.

 test.support.import_helper.unload(*name*)

Strip *name* out of `sys.modules`.

 test.support.import_helper.make_legacy_pyc(*source*)

Relocate a [**PEP 3147**](https://peps.python.org/pep-3147/)/[**PEP 488**](https://peps.python.org/pep-0488/) pyc file to where the legacy pyc would sit, then give back the filesystem path of that legacy pyc file. The *source* value holds the filesystem path of the source file. That source file is not obliged to exist, but the PEP 3147/488 pyc file does have to be present.

[Subject index](INDEX.md) · [Previous](../test-support-os-helper/os-test-tree-and-file-removal-helpers.md) · [Continue](test-support-import-helper-cleanimport-class.md)
