# What’s New In Python 3.8 / Optimizations — os, subprocess

### Optimizations

- In certain situations the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module can henceforth call the [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) function for a performance boost. For now it kicks in solely on macOS and Linux (with glibc 2.24 or later) provided each of these requirements holds:

  - *close_fds* is false;

  - the *preexec_fn*, *pass_fds*, *cwd* and *start_new_session* parameters are left unset;

  - a directory appears in the *executable* path.

(Contributed by Joannah Nanjekye and Victor Stinner in [bpo-35537](https://bugs.python.org/issue?@action=redirect&bpo=35537).)

-

On Linux and macOS, [`shutil.copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile), [`shutil.copy()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy), [`shutil.copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2), [`shutil.copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree) and [`shutil.move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) now rely on platform-specific "fast-copy" syscalls so the data moves more efficiently. The "fast-copy" label means the transfer stays inside the kernel and skips the userspace buffers that Python would otherwise allocate, as happens with "`outfd.write(infd.read())`". Under Windows, `shutil.copyfile()` adopts a larger default buffer (1 MiB rather than 16 KiB) together with a [`memoryview()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview)-based form of [`shutil.copyfileobj()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfileobj). Copying a 512 MiB file inside one partition gets roughly +26% quicker on Linux, +50% on macOS and +40% on Windows. CPU cycle usage also drops considerably. Consult the [Platform-dependent efficient copy operations](https://docs.python.org/3.14/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section. (Contributed by Giampaolo Rodol?? in [bpo-33671](https://bugs.python.org/issue?@action=redirect&bpo=33671).)

- [`shutil.copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree) now calls the [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) function, and every copy helper built on top of it reuses cached [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) values. Duplicating a directory holding 8000 files runs about +9% faster on Linux, +20% on Windows and +30% across a Windows SMB share. The count of `os.stat()` syscalls also falls by 38%, which makes `shutil.copytree()` notably quicker on network filesystems. (Contributed by Giampaolo Rodol?? in [bpo-33695](https://bugs.python.org/issue?@action=redirect&bpo=33695).)

- Within the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module the default is now Protocol 4, which arrived in Python 3.4. Relative to Protocol 3 (available since Python 3.0), it yields better performance plus a smaller serialized size.

- A single [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) member was dropped from `PyGC_Head`. Every GC tracked object (for instance tuple, list, dict) shrinks by 4 or 8 bytes. (Contributed by Inada Naoki in [bpo-33597](https://bugs.python.org/issue?@action=redirect&bpo=33597).)

- To shrink its memory footprint, [`uuid.UUID`](https://docs.python.org/3.14/library/uuid.html#uuid.UUID) now relies on `__slots__`. (Contributed by Wouter Bolsterlee and Tal Einat in [bpo-30977](https://bugs.python.org/issue?@action=redirect&bpo=30977))

- [`operator.itemgetter()`](https://docs.python.org/3.14/library/operator.html#operator.itemgetter) became 33% faster. Argument handling was optimized and a fast path was introduced for the frequent scenario of one non-negative integer index into a tuple (the usual pattern across the standard library). (Contributed by Raymond Hettinger in [bpo-35664](https://bugs.python.org/issue?@action=redirect&bpo=35664).)

- Field lookups in [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) were accelerated. They now run more than twice as quickly, which makes them the speediest way to access an instance variable in Python. Credited to the following contributors in [bpo-32492](https://bugs.python.org/issue?@action=redirect&bpo=32492): Raymond Hettinger, Pablo Galindo, and Joe Jevnik, Serhiy Storchaka.

- When the supplied iterable reports a known length (it implements `__len__`), the [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) constructor skips overallocating its internal item buffer. On average that trims the resulting list by 12%. (Contributed by Raymond Hettinger and Pablo Galindo in [bpo-33234](https://bugs.python.org/issue?@action=redirect&bpo=33234).)

- The speed of class variable writes was doubled. Updating a non-dunder attribute had been triggering a needless call that updated slots. This fix is recorded in [bpo-36012](https://bugs.python.org/issue?@action=redirect&bpo=36012), with thanks to Stefan Behnel, Pablo Galindo Salgado, Raymond Hettinger, Neil Schemenauer, and Serhiy Storchaka.

- The cost of converting arguments handed to many builtin functions and methods was cut. That made calling certain simple builtin functions and methods up to 20–50% quicker. (Contributed by Serhiy Storchaka in [bpo-23867](https://bugs.python.org/issue?@action=redirect&bpo=23867), [bpo-35582](https://bugs.python.org/issue?@action=redirect&bpo=35582) and [bpo-36127](https://bugs.python.org/issue?@action=redirect&bpo=36127).)

- The `LOAD_GLOBAL` instruction now relies on a new "per opcode cache" mechanism. As a result it runs roughly 40% faster. (Contributed by Yury Selivanov and Inada Naoki in [bpo-26219](https://bugs.python.org/issue?@action=redirect&bpo=26219).)

[Subject index](INDEX.md) · [Previous source section](xmlrpc.md) · [Release/subject declaration](assignment-expressions.md) · [Next source section](build-and-c-api-changes.md)
