# unittest — Test Discovery

### Test Discovery

Added in version 3.2.

Simple test discovery is supported by Unittest. For test files to work with test discovery, each one has to be a [module](https://docs.python.org/3.14/tutorial/modules.html#tut-modules) or [package](https://docs.python.org/3.14/tutorial/modules.html#tut-packages) that can be imported from the project's top-level directory (which means each filename has to be a valid [identifier](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers)).

The implementation of test discovery lives in `TestLoader.discover()`, yet it is usable from the command line too. Here is the basic command-line usage:

```python
cd project_directory
python -m unittest discover

```

Note

For convenience, `python -m unittest` amounts to the same thing as `python -m unittest discover`. Should you need to feed arguments to test discovery, you have to name the `discover` sub-command explicitly.

These are the options the `discover` sub-command accepts:

 -v, --verbose

Verbose output

 -s, --start-directory directory

Directory to start discovery (`.` default)

 -p, --pattern pattern

Pattern to match test files (`test*.py` default)

 -t, --top-level-directory directory

Top level directory of project (defaults to start directory)

You may give the `-s`, `-p`, and `-t` options as positional arguments, in that very order. The two command lines below mean the same thing:

```python
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"

```

Beyond passing a path, you can also give a package name as the start directory, for example `myproject.subpackage.test`. The package name you provide is then imported, and where it sits on the filesystem becomes the start directory.

Caution

To load tests, test discovery imports them. After test discovery has located every test file beneath the start directory you name, it converts the paths into package names so they can be imported. As an example, `foo/bar/baz.py` gets imported as `foo.bar.baz`.

Should a package already be installed globally while you run test discovery against a separate copy of that same package, the import *could* end up coming from the wrong location. When that occurs, test discovery warns you and exits.

Should you give the start directory as a package name instead of a directory path, then discover treats whatever location it imports from as the location you meant, so the warning never appears.

By means of the load_tests protocol, test modules and packages can tailor how tests are loaded and discovered.

Changed in version 3.4: Test discovery supports [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package).

Changed in version 3.11: Support for [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package) was removed from test discovery; it had been broken ever since Python 3.7. The start directory, along with any of its subdirectories holding tests, has to be a regular package carrying an `__init__.py` file.

When the start directory is the package's dotted name, the ancestor packages are allowed to be namespace packages.

Changed in version 3.14: Once more a [namespace package](https://docs.python.org/3.14/glossary.html#term-namespace-package) may serve as the start directory for test discovery. So that directories having nothing to do with Python aren't scanned, no search for tests happens in subdirectories lacking an `__init__.py`.

[Subject index](INDEX.md) · [Previous](command-line-options.md) · [Continue](test-code-organization-overview.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)
