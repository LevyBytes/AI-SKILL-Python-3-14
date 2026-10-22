# Python 3.10.0 beta 1 / c api / debug

[bpo-43774](https://bugs.python.org/issue?@action=redirect&bpo=43774): The now-unused `PYMALLOC_DEBUG` macro was removed. Whenever Python is built in debug mode (that is, with the `Py_DEBUG` macro defined), debug hooks on the memory allocators are now set up by default. They are also usable on a release-mode Python build (for example via the `PYTHONMALLOC=debug` environment variable).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
