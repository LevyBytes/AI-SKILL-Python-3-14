# warnings — Describing Warning Filters

### Describing Warning Filters

Setting up the warnings filter starts from the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) options given on the Python interpreter command line and from the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable. The interpreter stores every supplied entry, uninterpreted, in [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions); the `warnings` module then parses them on its first import (entries that are invalid get skipped, with a message printed to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) beforehand).

A single warnings filter is written as a series of fields, with colons between them:

```python
action:message:category:module:line

```

Each of these fields means what The Warnings Filter described above. If you put several filters on one line (the way [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) expects), separate them with commas; filters appearing later win over earlier ones (because they apply left-to-right, and whichever filter was applied most recently takes priority over the ones before it).

Frequently used warning filters target every warning, or warnings of one category, or warnings coming from specific modules or packages. A few examples:

```python
default                      # Show all warnings (even those ignored by default)
ignore                       # Ignore all warnings
error                        # Convert all warnings to errors
error::ResourceWarning       # Treat ResourceWarning messages as errors
default::DeprecationWarning  # Show DeprecationWarning messages
ignore,default:::mymodule    # Only report warnings triggered by "mymodule"
error:::mymodule             # Convert warnings to errors in "mymodule"

```

[Subject index](INDEX.md) · [Previous](repeated-warning-suppression-criteria.md) · [Continue](default-warning-filter.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
