# test.support.os_helper: Filesystem capability, working-directory and descriptor test helpers

test.support.os_helper.can_symlink()

Returns `True` when the OS handles symbolic links, and `False` otherwise.

 test.support.os_helper.can_xattr()

Returns `True` when the OS handles xattr, and `False` otherwise.

 test.support.os_helper.change_cwd(*path*, *quiet=False*)

A context manager that briefly switches the current working directory to *path* and yields that directory.

When *quiet* is `False`, the context manager raises an exception upon error. If not, it merely emits a warning and leaves the current working directory unchanged.

 test.support.os_helper.create_empty_file(*filename*)

Makes an empty file at *filename*. Should it already exist, it is truncated.

 test.support.os_helper.fd_count()

Counts how many file descriptors are open.

 test.support.os_helper.fs_is_case_insensitive(*directory*)

Returns `True` when the file system for *directory* ignores case.

 test.support.os_helper.make_bad_fd()

Produces an invalid file descriptor by opening and then closing a temporary file and returning its descriptor.

 test.support.os_helper.rmdir(*filename*)

[Subject index](INDEX.md) · [Previous](fake-path-and-environment-guard-helpers.md) · [Owning module, declaration or section: test.support.os_helper](filesystem-encoding-test-names.md) · [Required continuation of the source contract](os-test-tree-and-file-removal-helpers.md)
