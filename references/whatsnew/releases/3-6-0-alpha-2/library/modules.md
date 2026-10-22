# Python 3.6.0 alpha 2 / library / modules

[bpo-26373](https://bugs.python.org/issue?@action=redirect&bpo=26373): subprocess.Popen.communicate now properly disregards BrokenPipeError whenever the child process dies ahead of the .communicate() call across more or all situations.

- The signal, socket, and ssl modules now return a single consistent name when an IntEnum constant value maps to several names. For instance, signal.Signals(6) now always describes itself as signal.SIGALRM instead of toggling between that and signal.SIGIOT depending on the interpreter's hash randomization seed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
