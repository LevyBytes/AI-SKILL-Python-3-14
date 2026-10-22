# Python 3.14.0 alpha 1 / library / os

[bpo-45767](https://bugs.python.org/issue?@action=redirect&bpo=45767): Integer conversion is fixed in [`os.major()`](https://docs.python.org/3.14/library/os.html#os.major), [`os.minor()`](https://docs.python.org/3.14/library/os.html#os.minor), and [`os.makedev()`](https://docs.python.org/3.14/library/os.html#os.makedev). Device numbers above `2**63-1` are now handled, as is the non-existent device number (`NODEV`).

[bpo-41843](https://bugs.python.org/issue?@action=redirect&bpo=41843): On Solaris, the [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) fast-copy syscall is now leveraged to make the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) file-copy functions more efficient.

[gh-119169](https://github.com/python/cpython/issues/119169): Give [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk) a small speed boost by streamlining its exception handling.

[gh-120057](https://github.com/python/cpython/issues/120057): Introduce the [`os.environ.refresh()`](https://docs.python.org/3.14/library/os.html#os.environ) method that syncs `os.environ` with environment changes produced by [`os.putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv), by [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv), or made beyond Python within the same process. Victor Stinner contributed this.

[gh-89727](https://github.com/python/cpython/issues/89727): Address the case where [`os.fwalk()`](https://docs.python.org/3.14/library/os.html#os.fwalk) raised a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) on deeply nested directory trees, switching the implementation from recursive to iterative.

[gh-120743](https://github.com/python/cpython/issues/120743): [Soft deprecate](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) the [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) and [`os.spawn*`](https://docs.python.org/3.14/library/os.html#os.spawnl) functions. Fresh code ought to avoid them; reach for the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module as the suggested replacement. Victor Stinner authored the patch.

[gh-123014](https://github.com/python/cpython/issues/123014): [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open) together with [`signal.pidfd_send_signal()`](https://docs.python.org/3.14/library/signal.html#signal.pidfd_send_signal) are now absent when compiling against Android API levels below 31, because the backing system calls might trigger a crash.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
