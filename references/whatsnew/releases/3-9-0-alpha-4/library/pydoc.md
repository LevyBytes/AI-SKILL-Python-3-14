# Python 3.9.0 alpha 4 / library / pydoc

[bpo-21016](https://bugs.python.org/issue?@action=redirect&bpo=21016): The [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) plus [`trace`](https://docs.python.org/3.14/library/trace.html#module-trace) modules now consult the [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) module for the path to the Python standard library, which supports unusual install paths such as `/usr/lib64/python3.9/` on Fedora. Jan Matějek supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
