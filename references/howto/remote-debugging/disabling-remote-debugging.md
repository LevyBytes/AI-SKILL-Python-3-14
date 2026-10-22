# Disabling remote debugging

### Disabling remote debugging

Any one of the options below will turn off support for remote debugging:

- Before the interpreter launches, set the [`PYTHON_DISABLE_REMOTE_DEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_DISABLE_REMOTE_DEBUG) environment variable to a value of `1`.

- Pass the [`-X disable_remote_debug`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option on the command line.

- Build Python using the [`--without-remote-debug`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-remote-debug) configuration flag.

[Subject index](INDEX.md) · [Previous source context](remote-debugging-attachment-protocol.md) · [Following source context](permission-requirements.md)
