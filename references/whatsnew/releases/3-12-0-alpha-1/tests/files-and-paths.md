# Python 3.12.0 alpha 1 / tests / files and paths

[gh-93852](https://github.com/python/cpython/issues/93852): test_asyncio, test_logging, test_socket and test_socketserver now place AF_UNIX domains within the current directory so they stop failing with `OSError("AF_UNIX path too long")` when the temporary directory (the `TMPDIR` environment variable) is overly long. Victor Stinner wrote the patch.

[gh-93353](https://github.com/python/cpython/issues/93353): When invoked with the -jN option, regrtest now verifies whether a test leaks temporary files or directories. Victor Stinner wrote the patch.

[gh-90473](https://github.com/python/cpython/issues/90473): On WASI, skip the tests that need symlinks pointing to absolute paths.

[gh-90473](https://github.com/python/cpython/issues/90473): On WASI, skip the symlink tests. wasmtime invokes `openat2(2)` together with the `RESOLVE_BENEATH` flag, which blocks symlinks holding absolute paths.

[gh-92670](https://github.com/python/cpython/issues/92670): On AIX, skip the `test_shutil.TestCopy.test_copyfile_nonexistent_dir` test, since it appends a trailing slash to make the OS treat the path as a directory, yet under AIX that trailing slash does nothing and the path counts as a file.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
