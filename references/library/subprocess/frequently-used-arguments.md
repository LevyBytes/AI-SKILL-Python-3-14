# subprocess - Frequently Used Arguments

### Frequently Used Arguments

So that a broad range of scenarios can be served, both the `Popen` constructor and the convenience functions take a sizable set of optional arguments. In the bulk of everyday scenarios, a good many of these arguments can comfortably stay at their defaults. The ones you will reach for most are:

>

*args* has to be supplied on every call and should be either a string or a sequence of program arguments. Handing in a sequence of arguments is normally the better choice, since it lets the module handle whatever escaping and quoting the arguments need (for instance, to allow spaces in file names). When you pass just a single string, either *shell* has to be [`True`](https://docs.python.org/3.14/library/constants.html#True) (see below), or else that string can only name the program you want run, with no arguments attached.

*stdin*, *stdout* and *stderr* designate the standard input, standard output and standard error file handles, respectively, for the program being run. Acceptable values are `None`, `PIPE`, `DEVNULL`, an existing file descriptor (a positive integer), and an existing [file object](https://docs.python.org/3.14/glossary.html#term-file-object) holding a valid file descriptor. Under the default of `None`, nothing is redirected. `PIPE` means a fresh pipe to the child is to be created. `DEVNULL` means the special file [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) is to be used. On top of that, *stderr* may be `STDOUT`, which routes the child process's stderr stream into whichever file handle already serves *stdout*.

When *encoding* or *errors* is given, or when *text* (otherwise called *universal_newlines*) is true, the file objects *stdin*, *stdout* and *stderr* open in text mode, using whichever *encoding* and *errors* the call specifies or the defaults belonging to [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper).

On *stdin*, the line ending characters `'\n'` within the input get translated to the default line separator [`os.linesep`](https://docs.python.org/3.14/library/os.html#os.linesep). On *stdout* and *stderr*, every line ending within the output gets translated to `'\n'`. For more detail, consult the documentation of the [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) class for the case where its constructor's *newline* argument is `None`.

When text mode is not in effect, *stdin*, *stdout* and *stderr* open as binary streams. Neither encoding nor line ending translation happens.

Changed in version 3.6: Added the *encoding* and *errors* parameters.

Changed in version 3.7: Added the *text* parameter as an alias for *universal_newlines*.

Note

The `Popen.communicate()` method does not refresh the newlines attribute of the file objects `Popen.stdin`, `Popen.stdout` and `Popen.stderr`.

When *shell* is `True`, the command you name runs by way of the shell. That can be handy when you lean on Python chiefly for the richer control flow it provides over most system shells, yet still want easy access to other shell amenities such as shell pipes, filename wildcards, expansion of environment variables, and expansion of `~` to a user's home directory. Bear in mind, though, that Python ships its own versions of many shell-like features (in particular, [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob), [`fnmatch`](https://docs.python.org/3.14/library/fnmatch.html#module-fnmatch), [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk), [`os.path.expandvars()`](https://docs.python.org/3.14/library/os.path.html#os.path.expandvars), [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser), and [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil)).

Changed in version 3.3: With *universal_newlines* set to `True`, the encoding the class applies is [`locale.getpreferredencoding(False)`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding) rather than `locale.getpreferredencoding()`. For further detail on this change, consult the [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) class.

Note

Read the Security Considerations section before using `shell=True`.

These options, together with all the rest, get fuller treatment in the `Popen` constructor documentation.

[Subject index](INDEX.md) · [Previous](subprocess-devnull-to-subprocess-calledprocesserror.md) · [Continue](popen-constructor.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
