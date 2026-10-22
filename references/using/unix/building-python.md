# 2.2. Building Python

### 2.2. Building Python

See also

Planning to contribute to CPython? Turn to the [devguide](https://devguide.python.org/getting-started/setup-building/); it covers how to build plus further pointers for getting your environment ready.

To build CPython on your own, the first step is obtaining the [source](https://www.python.org/downloads/source/). Either pull down the source of the most recent release or make a fresh [clone](https://devguide.python.org/setup/#get-the-source-code). On top of that, you will have to install the [build requirements](https://docs.python.org/3.14/using/configure.html#build-requirements).

Building it relies on the familiar sequence of commands:

```sh
./configure
make
make install

```

The [Configuration options](https://docs.python.org/3.14/using/configure.html#configure-options), along with platform-specific gotchas for the various Unix systems, are spelled out at length in the [README.rst](https://github.com/python/cpython/tree/3.14/README.rst) file sitting at the top of the Python source tree.

Warning

Running `make install` may clobber or shadow the `python3` binary. For that reason, favor `make altinstall` over `make install`, because it lays down only `*exec_prefix*/bin/python*version*`.

[Subject index](INDEX.md) · [Previous source section](on-freebsd-and-openbsd.md) · [Following source section](python-related-paths-and-files.md)
