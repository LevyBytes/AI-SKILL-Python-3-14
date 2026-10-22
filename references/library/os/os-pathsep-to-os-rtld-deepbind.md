# os: `os.pathsep`, `os.defpath`, `os.linesep`, `os.devnull`, `os.RTLD_LAZY`, `os.RTLD_NOW`, `os.RTLD_GLOBAL`, `os.RTLD_LOCAL`, `os.RTLD_NODELETE`, `os.RTLD_NOLOAD`, `os.RTLD_DEEPBIND`

os.pathsep

The character that, by convention, the operating system relies on to part components of a search path (as in `PATH`): for POSIX this is `':'`, while for Windows it is `';'`. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.defpath

The default search path that `exec*p*` and `spawn*p*` use when the environment carries no `'PATH'` key. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.linesep

The string used to part (or rather, terminate) lines on the current platform. This might be one character, such as `'\n'` for POSIX, or several characters, for instance `'\r\n'` for Windows. Do not use *os.linesep* as a line terminator while writing files opened in text mode (the default); on every platform, use a single `'\n'` instead.

 os.devnull

The file path of the null device. As an example: `'/dev/null'` for POSIX, `'nul'` for Windows. Also available via [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

 os.RTLD_LAZY

 os.RTLD_NOW

 os.RTLD_GLOBAL

 os.RTLD_LOCAL

 os.RTLD_NODELETE

 os.RTLD_NOLOAD

 os.RTLD_DEEPBIND

Flags meant for use with the [`setdlopenflags()`](https://docs.python.org/3.14/library/sys.html#sys.setdlopenflags) and [`getdlopenflags()`](https://docs.python.org/3.14/library/sys.html#sys.getdlopenflags) functions. The Unix manual page *[dlopen(3)](https://manpages.debian.org/dlopen(3))* explains what each flag means.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](os-confstr-to-os-extsep.md) · [Continue](os-getrandom-to-os-urandom.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Miscellaneous System Information](os-confstr-to-os-extsep.md)
