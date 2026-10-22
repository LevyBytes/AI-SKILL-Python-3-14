# Installation

### Installation

From Python 3.13 onward, the official installers for macOS and Windows let you choose to add free-threaded Python binaries during setup. Grab those installers from [https://www.python.org/downloads/](https://www.python.org/downloads/).

If you're on a different platform, refer to [Installing a Free-Threaded Python](https://py-free-threading.github.io/installing-cpython/), a community-kept walkthrough covering how to set up free-threaded Python.

To compile CPython yourself and get a free-threaded interpreter, pass the [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) configure flag.

[Subject index](INDEX.md) · [Previous source context](python-support-for-free-threading.md) · [Following source context](identifying-free-threaded-python.md)
