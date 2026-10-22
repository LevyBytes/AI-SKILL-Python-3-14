# What’s New in Python 2.6 / Deprecations and Removals — email, fcntl, hashlib, subprocess

### Deprecations and Removals

- String exceptions are gone. Trying to use one now raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

- Work on the [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) interface mandated by [**PEP 352**](https://peps.python.org/pep-0352/) is still ongoing. In 2.6, the `message` attribute is on the way out, with the [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) attribute taking over.

- (3.0-warning mode) The standard library gets reshuffled in Python 3.0, with a number of stale modules dropped and others renamed. When run in 3.0-warning mode, Python 2.6 emits a warning each time one of these modules is imported.

The modules flagged as deprecated are: `audiodev`, `bgenlocations`, `buildtools`, `bundlebuilder`, `Canvas`, `compiler`, `dircache`, `dl`, `fpformat`, `gensuitemodule`, `ihooks`, `imageop`, `imgfile`, `linuxaudiodev`, `mhlib`, `mimetools`, `multifile`, `new`, `pure`, `statvfs`, `sunaudiodev`, `test.testall`, and `toaiff`.

- The `gopherlib` module is gone.

- Both the `MimeWriter` module and the `mimify` module are now deprecated; reach for the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package in their place.

- The `md5` module is now deprecated; turn to the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module instead.

- The `posixfile` module is now deprecated; [`fcntl.lockf()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.lockf) does a better job of locking.

- The `popen2` module is now deprecated; reach for the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module.

- The `rgbimg` module is gone.

- The `sets` module is now deprecated; you are better off with the built-in [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) and [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) types.

- The `sha` module is now deprecated; turn to the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module instead.

[Subject index](INDEX.md) · [Previous source section](improved-ssl-support.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](python-3-0.md)
