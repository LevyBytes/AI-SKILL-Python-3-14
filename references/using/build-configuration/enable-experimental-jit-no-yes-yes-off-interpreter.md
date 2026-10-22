# --enable-experimental-jit=[no/yes/yes-off/interpreter]

--enable-experimental-jit=[no|yes|yes-off|interpreter]

Specify the manner of integrating the [experimental just-in-time compiler](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-jit-compiler).

- `no`: Don’t build the JIT.

- `yes`: Build the JIT enabled. To turn it off at runtime, assign the environment variable [`PYTHON_JIT=0`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_JIT).

- `yes-off`: Build the JIT but leave it off by default. To turn it on at runtime, assign the environment variable [`PYTHON_JIT=1`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_JIT).

- `interpreter`: Switch on the “JIT interpreter” (helpful only when debugging the JIT itself). To turn it off at runtime, assign the environment variable [`PYTHON_JIT=0`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_JIT).

When the option is omitted, the default behavior is `--enable-experimental-jit=no`, while `--enable-experimental-jit` serves as a shorthand for `--enable-experimental-jit=yes`. Consult `Tools/jit/README.md` for further information, such as how to set up the build-time dependencies you will need.

Note

While compiling CPython with the JIT enabled, make sure your machine already has Python 3.11 or a newer release installed.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source section](disable-gil.md) · [Following source section](pkg-config.md)
