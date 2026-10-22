# os: `os.EX_USAGE`, `os.EX_DATAERR`, `os.EX_NOINPUT`, `os.EX_NOUSER`, `os.EX_NOHOST`, `os.EX_UNAVAILABLE`, `os.EX_SOFTWARE`, `os.EX_OSERR`, `os.EX_OSFILE`, `os.EX_CANTCREAT`, `os.EX_IOERR`, `os.EX_TEMPFAIL`, `os.EX_PROTOCOL`, `os.EX_NOPERM`

os.EX_USAGE

Exit code signaling that the command was misused, for instance when the argument count is wrong.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_DATAERR

Exit code that means the input data was incorrect.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_NOINPUT

Exit code signaling that an input file was absent or could not be read.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_NOUSER

Exit code that means a specified user did not exist.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_NOHOST

Exit code that means a specified host did not exist.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_UNAVAILABLE

Exit code that means that a required service is unavailable.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_SOFTWARE

Exit code that means an internal software error was detected.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_OSERR

Exit code signaling that an operating system error showed up, for instance a failure to fork or to create a pipe.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_OSFILE

Exit code signaling that some system file was absent, would not open, or ran into some other error.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_CANTCREAT

Exit code signaling that a user-specified output file was not able to be created.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_IOERR

Exit code signaling that an error came up while performing I/O on some file.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_TEMPFAIL

Exit code signaling that a temporary failure showed up. This flags something that may not truly be an error, for instance a network connection that could not be established during a retryable operation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_PROTOCOL

Exit code signaling that a protocol exchange was illegal, invalid, or beyond comprehension.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.EX_NOPERM

Exit code signaling that permissions were too limited to carry out the operation (though not meant for file system problems).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

[Subject index](INDEX.md) · [Previous](os-abort-to-os-ex-ok.md) · [Continue](os-ex-config-to-os-forkpty.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
