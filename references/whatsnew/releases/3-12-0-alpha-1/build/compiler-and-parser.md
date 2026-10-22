# Python 3.12.0 alpha 1 / build / compiler and parser

[gh-96761](https://github.com/python/cpython/issues/96761): Repair the clang compiler build flow for **_bootstrap_python** whenever LTO optimization is in effect. Matthias Görgens and Donghee Na wrote the patch.

[gh-85936](https://github.com/python/cpython/issues/85936): Whenever the Clang compiler honors the flag, CPython now defaults to the ThinLTO option as its policy. Donghee Na wrote the patch.

[gh-93202](https://github.com/python/cpython/issues/93202): For rendering a `size_t` or `Py_ssize_t` value, Python now relies solely on the `%zu` and `%zd` printf formats. Since a C11 compiler is mandatory to build Python 3.12, support for those printf formats is now guaranteed. Victor Stinner supplied the patch.

[bpo-34449](https://bugs.python.org/issue?@action=redirect&bpo=34449): The bogus `-fPIC` compiler switch is dropped for HP aCC on HP-UX. Michael Osipov authored this fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
