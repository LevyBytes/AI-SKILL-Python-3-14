# Python 3.5.0 alpha 4 / library / functions and types

[bpo-23193](https://bugs.python.org/issue?@action=redirect&bpo=23193): Introduce a numeric_owner parameter onto tarfile.TarFile.extract together with tarfile.TarFile.extractall. Michael Vogt and Eric Smith wrote the patch.

[bpo-23342](https://bugs.python.org/issue?@action=redirect&bpo=23342): Introduce a subprocess.run() function that yields a CalledProcess instance, giving a more uniform API than the current call* functions.

[bpo-21217](https://bugs.python.org/issue?@action=redirect&bpo=21217): inspect.getsourcelines() now attempts deriving the starting and ending lines straight from the code object, which resolves a problem where a lambda serves as a decorator argument. Thomas Ballinger and Allison Kaptur wrote the patch.

[bpo-23834](https://bugs.python.org/issue?@action=redirect&bpo=23834): Repair socket.sendto() so the C Py_ssize_t type, rather than the C int type, holds the sendto() result.

[bpo-21526](https://bugs.python.org/issue?@action=redirect&bpo=21526): The new boolean type from Tcl 8.5 is now supported by Tkinter.

[bpo-23611](https://bugs.python.org/issue?@action=redirect&bpo=23611): Pickle protocols < 4 now cover serialization of more "lookupable" objects, including unbound methods or nested classes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
