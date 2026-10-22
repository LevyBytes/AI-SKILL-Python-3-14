# Compiling and Linking under Unix-like systems

### 1.6. Compiling and Linking under Unix-like systems

Tracking down the correct flags for your compiler (and linker) so as to embed the Python interpreter in your application is not always straightforward, in large part because Python has to load library modules built as C dynamic extensions (`.so` files) linked against it.

To learn which compiler and linker flags you need, run the `python*X.Y*-config` script that installation produces (a `python3-config` script might be on hand too). That script offers several options, and these are the ones of immediate use to you:

- `pythonX.Y-config --cflags` hands you the flags advised for compiling:

```shell
$ /opt/bin/python3.11-config --cflags
-I/opt/include/python3.11 -I/opt/include/python3.11 -Wsign-compare  -DNDEBUG -g -fwrapv -O3 -Wall

```

- `pythonX.Y-config --ldflags --embed` hands you the flags advised for linking:

```shell
$ /opt/bin/python3.11-config --ldflags --embed
-L/opt/lib/python3.11/config-3.11-x86_64-linux-gnu -L/opt/lib -lpython3.11 -lpthread -ldl  -lutil -lm

```

Note

So as not to mix up multiple Python installations (above all the system Python versus one you compiled yourself), the advice is to give the absolute path to `python*X.Y*-config`, just as the example above shows.

Should this approach fall short for you (it carries no promise of working on every Unix-like platform, though [bug reports](https://docs.python.org/3.14/bugs.html#reporting-bugs) are welcome), you will need to study your system's documentation on dynamic linking and/or look over Python's `Makefile` (locate it with [`sysconfig.get_makefile_filename()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_makefile_filename)) along with its compilation options. Here the [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) module comes in handy for pulling out, in code, the configuration values you will want to stitch together. As an example:

```pycon
>>> import sysconfig
>>> sysconfig.get_config_var('LIBS')
'-lpthread -ldl  -lutil'
>>> sysconfig.get_config_var('LINKFORSHARED')
'-Xlinker -export-dynamic'

```

[Subject index](INDEX.md) · [Previous source section](embedding-python-in-c.md)
