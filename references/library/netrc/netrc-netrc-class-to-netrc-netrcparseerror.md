# netrc — `netrc` — netrc file processing

### `netrc` — netrc file processing

**Source code:** [Lib/netrc.py](https://github.com/python/cpython/tree/3.14/Lib/netrc.py)

---

Reading and wrapping the netrc file format that the Unix **ftp** tool and other FTP clients rely on is the job of the `netrc` class.

 *class *netrc.netrc([*file*])

Data drawn from a netrc file is wrapped up by a `netrc` instance, whether of the class itself or a subclass. When the constructor argument is supplied, it names the file to read. With no argument, what gets read is `.netrc` inside the home directory of the user, located through [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser); if that file is absent a [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is thrown. A `NetrcParseError`, complete with diagnostics covering the file name, the line number, and the terminating token, is raised on parse problems.

On a POSIX system with no argument passed, finding passwords in `.netrc` triggers a `NetrcParseError` whenever that file's ownership or permissions are unsafe — that is, owned by someone other than the process's own user, or readable or writable by anybody else. The behavior here matches the safeguards ftp and similar `.netrc` consumers apply. Platforms lacking [`os.getuid()`](https://docs.python.org/3.14/library/os.html#os.getuid) cannot perform these checks.

Changed in version 3.4: Added the POSIX permission check.

Changed in version 3.7: When *file* is left out, [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) now determines where the `.netrc` file sits.

Changed in version 3.10: `netrc` now attempts UTF-8 first and only falls back to the locale-specific encoding. A netrc entry is no longer required to list every token; any token left out simply defaults to an empty string. Tokens and their values may now hold any characters at all, whitespace and non-ASCII included. A login name of anonymous skips the security check.

 *exception *netrc.NetrcParseError

Thrown by the `netrc` class once it runs into syntax errors within the source text. Each instance of it carries three notable attributes:

 msg

Textual explanation of the error.

 filename

The name of the source file.

 lineno

The line number on which the error was found.

[Subject index](INDEX.md) · [Previous](netrc-file-processing.md) · [Continue](netrc-authenticators-to-netrc-macros.md)
