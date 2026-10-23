# What's New In Python 3.4 / PEP 446: Newly Created File Descriptors Are Non-Inheritable - os, socket

### PEP 446: Newly Created File Descriptors Are Non-Inheritable

[**PEP 446**](https://peps.python.org/pep-0446/) renders freshly created file descriptors [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance). Typically this is exactly what an application wants: when spawning a new process, leaving currently open files also open within the new process can produce all manner of elusive bugs, and possibly security problems too.

Nevertheless, inheritance is sometimes wanted. The following new functions and methods exist to cover those scenarios:

- [`os.get_inheritable()`](https://docs.python.org/3.14/library/os.html#os.get_inheritable), [`os.set_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_inheritable)

- [`os.get_handle_inheritable()`](https://docs.python.org/3.14/library/os.html#os.get_handle_inheritable), [`os.set_handle_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_handle_inheritable)

- [`socket.socket.get_inheritable()`](https://docs.python.org/3.14/library/socket.html#socket.socket.get_inheritable), [`socket.socket.set_inheritable()`](https://docs.python.org/3.14/library/socket.html#socket.socket.set_inheritable)

See also

[**PEP 446**](https://peps.python.org/pep-0446/): Make newly created file descriptors non-inheritable

PEP written and implemented by Victor Stinner.

[Subject index](INDEX.md) · [Previous source section](pep453-pip-documentation.md) · [Next source section](improvements-to-codec-handling.md) · [Release/subject declaration](release-highlights.md)
