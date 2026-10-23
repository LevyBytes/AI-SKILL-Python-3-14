# readline - Init file

### Init file

The functions below concern the init file and user-supplied configuration:

 readline.parse_and_bind(*string*)

Run the init line given through the *string* argument. Underneath, this invokes `rl_parse_and_bind()` in the library.

 readline.read_init_file([*filename*])

Run a readline initialization file. When no filename is given, the most recently used filename applies. This invokes `rl_read_init_file()` in the underlying library. It raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `open` carrying the file name when one is supplied, and `"<readline_init_file>"` if not, no matter which file the library ends up resolving.

Changed in version 3.14: The auditing event was added.

[Subject index](INDEX.md) · [Previous](readline-backend.md) · [Continue](readline-get-line-buffer-to-readline-redisplay.md) · [Owning module, declaration or section: readline](readline-backend.md)
