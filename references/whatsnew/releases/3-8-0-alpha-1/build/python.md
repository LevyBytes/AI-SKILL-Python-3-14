# Python 3.8.0 alpha 1 / build / python

[bpo-33012](https://bugs.python.org/issue?@action=redirect&bpo=33012): gcc 8 introduced a fresh warning heuristic that spots invalid function casts, and a stock python build appears to trip that warning fairly frequently. The most frequent is casting a METH_NOARGS function (which takes only one argument) into a PyCFunction. Resolve this by appending a dummy argument onto every function implementing METH_NOARGS.

[bpo-32898](https://bugs.python.org/issue?@action=redirect&bpo=32898): Repair the python debug build whenever COUNT_ALLOCS is in use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
