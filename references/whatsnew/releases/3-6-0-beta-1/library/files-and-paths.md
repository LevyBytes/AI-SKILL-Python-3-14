# Python 3.6.0 beta 1 / library / files and paths

[bpo-27842](https://bugs.python.org/issue?@action=redirect&bpo=27842): Rows from csv.DictReader are now of type OrderedDict. Steve Holden contributed this.

- Drop the ability to hand a file descriptor to os.access. That never functioned, yet earlier it raised nothing.

[bpo-26667](https://bugs.python.org/issue?@action=redirect&bpo=26667): importlib.util gained support for path-like objects.

[bpo-18401](https://bugs.python.org/issue?@action=redirect&bpo=18401): Pdb gained the ‘readrc’ keyword argument that governs whether .pdbrc files get read. Martin Matusiak and Sam Kimbrel wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
