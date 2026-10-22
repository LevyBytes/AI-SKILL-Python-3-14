# Python 3.5.0 alpha 1 / build / files and paths

[bpo-15234](https://bugs.python.org/issue?@action=redirect&bpo=15234): When building against BerkeleyDB and Sqlite, the located library and include paths are now appended only when they are not already on the search path. Doing so sidesteps adding an unnecessary runtime dependency on the library.

[bpo-17219](https://bugs.python.org/issue?@action=redirect&bpo=17219): Added a library build directory for cross-builds of Python extensions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
