# os - Inheritance of File Descriptors

### Inheritance of File Descriptors

Added in version 3.4.

Every file descriptor carries an "inheritable" flag that marks whether child processes may inherit the file descriptor. Beginning with Python 3.4, file descriptors that Python creates are non-inheritable by default.

On UNIX, non-inheritable file descriptors are closed in child processes when a new program is executed, whereas the rest are inherited. Keep in mind that non-inheritable file descriptors are nevertheless *inherited* by child processes across `os.fork()`.

On Windows, a child process closes its non-inheritable handles and file descriptors, except for the standard streams (file descriptors 0, 1 and 2, meaning stdin, stdout and stderr), each of which is always inherited. When the `spawn*` functions are used, every inheritable handle and every inheritable file descriptor is inherited. When the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module is used, every file descriptor other than the standard streams is closed, and inheritable handles are inherited only when the *close_fds* parameter is `False`.

On WebAssembly platforms, the file descriptor is unmodifiable.

 os.get_inheritable(*fd*, */*)

Read the "inheritable" flag of the given file descriptor (a boolean).

 os.set_inheritable(*fd*, *inheritable*, */*)

Assign the "inheritable" flag of the given file descriptor.

 os.get_handle_inheritable(*handle*, */*)

Read the "inheritable" flag of the given handle (a boolean).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 os.set_handle_inheritable(*handle*, *inheritable*, */*)

Assign the "inheritable" flag of the given handle.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

[Subject index](INDEX.md) · [Previous](os-terminal-size-class.md) · [Continue](os-access.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
