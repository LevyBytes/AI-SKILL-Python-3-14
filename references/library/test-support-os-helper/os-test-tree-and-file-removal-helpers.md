# test.support.os_helper: Temporary directories, permissions and file-removal test helpers

Invoke [`os.rmdir()`](https://docs.python.org/3.14/library/os.html#os.rmdir) against *filename*. Under Windows, a polling loop watching whether the file still exists surrounds the call; that loop is required because antivirus software may keep files open and block their removal.

 test.support.os_helper.rmtree(*path*)

Run [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) over *path*, or alternatively use [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) together with [`os.rmdir()`](https://docs.python.org/3.14/library/os.html#os.rmdir), to clear away a path along with everything inside it. Just like `rmdir()`, on Windows the operation is enclosed in a polling loop that watches whether the files are still present.

 @test.support.os_helper.skip_unless_symlink

A decorator meant for tests that depend on symbolic-link support being available.

 @test.support.os_helper.skip_unless_xattr

A decorator meant for tests that depend on xattr support being available.

 test.support.os_helper.temp_cwd(*name='tempcwd'*, *quiet=False*)

A context manager that, for the duration of its block, spins up a fresh directory and switches the current working directory (CWD) into it.

Within the current directory the context manager makes a throwaway directory called *name*, then briefly moves the working directory there. Should *name* be `None`, that throwaway directory is produced via [`tempfile.mkdtemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp).

When *quiet* is `False` and the CWD can neither be created nor switched, an error gets raised. In the opposite case only a warning surfaces and the original CWD stays in effect.

 test.support.os_helper.temp_dir(*path=None*, *quiet=False*)

A context manager that builds a throwaway directory located at *path* and then yields it.

Where *path* is `None`, the throwaway directory comes from [`tempfile.mkdtemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp). Where *quiet* is `False`, any error makes the context manager raise an exception. Otherwise, should *path* be given yet prove impossible to create, nothing more than a warning is emitted.

 test.support.os_helper.temp_umask(*umask*)

A context manager that, while its block runs, overrides the process umask.

 test.support.os_helper.unlink(*filename*)

Invoke [`os.unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink) against *filename*. Mirroring `rmdir()`, on Windows the call sits inside a polling loop that watches for the file's continued presence.

[Subject index](INDEX.md) · [Continue](../test-support-import-helper/import-test-cache-and-bytecode-helpers.md) · [Owning module, declaration or section: test.support.os_helper](filesystem-encoding-test-names.md) · [Owning module, declaration or section: test.support.os_helper.rmdir](os-test-symlink-and-directory-helpers.md) · [Preceding source contract and version conditions](os-test-symlink-and-directory-helpers.md)
