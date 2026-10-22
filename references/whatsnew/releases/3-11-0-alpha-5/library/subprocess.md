# Python 3.11.0 alpha 5 / library / subprocess

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) now pulls in the Windows-specific imports whenever the `msvcrt` module exists, and the POSIX-specific imports on every other platform. The result is a tidy exception when `_posixsubprocess` is missing (for instance, the Emscripten browser target).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
