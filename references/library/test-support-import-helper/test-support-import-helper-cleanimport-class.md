# test.support.import_helper: `test.support.import_helper.CleanImport`

*class *test.support.import_helper.CleanImport(**module_names*)

A context manager that compels import to yield a fresh module reference. It comes in handy when you want to exercise module-level behavior, for example whether a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) fires during import. Example usage:

```python
with CleanImport('foo'):
    importlib.import_module('foo')  # New reference.

```

[Subject index](INDEX.md) · [Previous](import-test-cache-and-bytecode-helpers.md) · [Continue](test-support-import-helper-dirsonsyspath-class.md) · [Owning module, declaration or section: test.support.import_helper](import-test-cache-and-bytecode-helpers.md)
