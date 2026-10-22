# sys.argv

sys.argv

The roster of command line arguments handed to a Python script. `argv[0]` holds the script name (whether that is a full pathname depends on the operating system). When the interpreter was launched with the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) command line option, `argv[0]` becomes the string `'-c'`. When no script name reached the Python interpreter, `argv[0]` is the empty string.

For iterating over standard input, or over the files listed on the command line, turn to the [`fileinput`](https://docs.python.org/3.14/library/fileinput.html#module-fileinput) module.

See also `sys.orig_argv`.

Note

Under Unix, the OS delivers command line arguments as bytes. Python decodes these using the filesystem encoding together with the “surrogateescape” error handler. To recover the raw bytes, fetch them via `[os.fsencode(arg) for arg in sys.argv]`.

[API family](INDEX.md) · [sys context index](../INDEX.md).
