# Python 3.14.0 alpha 1 / library / shutil

[gh-117151](https://github.com/python/cpython/issues/117151): On platforms other than Windows, the standard buffer size that [`shutil.copyfileobj()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfileobj) relies on grew from 64k up to 256k. Windows had already used a bigger value.

[gh-123084](https://github.com/python/cpython/issues/123084): Mark `shutil.ExecError` as deprecated; no [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) function has emitted it since Python 3.4. The name now stands as an alias for [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

[gh-89727](https://github.com/python/cpython/issues/89727): Fix the case where [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) threw a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) on deeply nested directory trees.

[gh-89727](https://github.com/python/cpython/issues/89727): Partially address the case where [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) raised a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) on deeply nested directory trees. The recursion error no longer appears whenever `rmtree.avoids_symlink_attacks` is false.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
