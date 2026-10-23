# What's New In Python 3.3 / PEP 3151: Reworking the OS and IO exception hierarchy - errno, select, socket

### PEP 3151: Reworking the OS and IO exception hierarchy

The set of exceptions thrown for operating system errors has been made both simpler and more fine-grained at once.

No longer must you agonize over picking the right exception type among [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError), [`EnvironmentError`](https://docs.python.org/3.14/library/exceptions.html#EnvironmentError), [`WindowsError`](https://docs.python.org/3.14/library/exceptions.html#WindowsError), `mmap.error`, [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error) or [`select.error`](https://docs.python.org/3.14/library/select.html#select.error). Those exception types have all collapsed into a single one: `OSError`. For compatibility's sake the remaining names survive as aliases.

What's more, pinning down one particular error condition has gotten simpler. Rather than checking the `errno` attribute (or `args[0]`) against some constant out of the [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) module, you can trap the fitting [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) subclass. Here are the subclasses on offer:

- [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError)

- [`ChildProcessError`](https://docs.python.org/3.14/library/exceptions.html#ChildProcessError)

- [`ConnectionError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionError)

- [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError)

- [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError)

- [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError)

- [`IsADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#IsADirectoryError)

- [`NotADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#NotADirectoryError)

- [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError)

- [`ProcessLookupError`](https://docs.python.org/3.14/library/exceptions.html#ProcessLookupError)

- [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError)

And [`ConnectionError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionError) on its own carries more fine-grained subclasses:

- [`BrokenPipeError`](https://docs.python.org/3.14/library/exceptions.html#BrokenPipeError)

- [`ConnectionAbortedError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionAbortedError)

- [`ConnectionRefusedError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionRefusedError)

- [`ConnectionResetError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionResetError)

Because of these new exceptions, the typical reasons to reach for [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) can now be sidestepped. Take this snippet, which was written for Python 3.2:

```python
from errno import ENOENT, EACCES, EPERM

try:
    with open("document.txt") as f:
        content = f.read()
except IOError as err:
    if err.errno == ENOENT:
        print("document.txt file is missing")
    elif err.errno in (EACCES, EPERM):
        print("You are not allowed to read document.txt")
    else:
        raise

```

it can now be expressed with neither the [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) import nor any hand inspection of exception attributes:

```python
try:
    with open("document.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("document.txt file is missing")
except PermissionError:
    print("You are not allowed to read document.txt")

```

See also

[**PEP 3151**](https://peps.python.org/pep-3151/) - Reworking the OS and IO Exception Hierarchy

PEP written and implemented by Antoine Pitrou

[Subject index](INDEX.md) · [Previous source section](pep-397-python-launcher-for-windows.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pep-380-syntax-for-delegating-to-a-subgenerator.md)
