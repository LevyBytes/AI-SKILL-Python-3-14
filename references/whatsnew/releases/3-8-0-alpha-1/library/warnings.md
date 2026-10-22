# Python 3.8.0 alpha 1 / library / warnings

[bpo-33375](https://bugs.python.org/issue?@action=redirect&bpo=33375): The warnings module now locates the Python file tied to a warning through the code object instead of the frame's global namespace. That matches the way tracebacks and pdb resolve filenames, and behaves better for code executed dynamically.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
