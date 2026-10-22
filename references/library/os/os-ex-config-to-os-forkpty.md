# os: `os.EX_CONFIG`, `os.EX_NOTFOUND`, `os.fork()`, `os.forkpty()`

os.EX_CONFIG

Exit code that means that some kind of configuration error occurred.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_NOTFOUND

Exit code that means something like "an entry was not found".

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.fork()

Fork a child process. Give back `0` in the child and the child's process id in the parent. Should an error occur, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

Note that a few platforms, FreeBSD <= 6.3 and Cygwin among them, carry known issues around using `fork()` from a thread.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.fork` with no arguments.

Warning

Should you use TLS sockets in an application calling `fork()`, consult the warning in the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) documentation.

Warning

On macOS, mixing this function with the use of higher-level system APIs makes it unsafe, and [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) counts among those.

Changed in version 3.8: A `fork()` call within a subinterpreter is no longer supported ([`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised).

Changed in version 3.12: Should Python manage to detect that your process has multiple threads, `os.fork()` now raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

We elected to raise this as a warning, where it can be detected, so as to better alert developers to a design problem the POSIX platform explicitly marks as unsupported. Even where code *appears* to work, combining threading with `os.fork()` on POSIX platforms has never been safe. The CPython runtime itself has always issued API calls (such as `malloc` and `free`) that are unsafe to use in the child process whenever threads were present in the parent.

Among those already more prone to hitting deadlocks while running such code are macOS users, along with users of libc or malloc implementations apart from the ones usually found in glibc to date.

Consult [this discussion on fork being incompatible with threads](https://discuss.python.org/t/33555) for the technical reasons we are bringing this long-standing platform compatibility problem to developers' attention.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX, not WASI, not Android, not iOS.

 os.forkpty()

[Subject index](INDEX.md) · [Previous](os-ex-usage-to-os-ex-noperm.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md) · [Required continuation of the source contract](os-kill-to-os-plock.md)
