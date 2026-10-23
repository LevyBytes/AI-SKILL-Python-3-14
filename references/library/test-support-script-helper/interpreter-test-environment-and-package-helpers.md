# test.support.script_helper`test.support.script_helper` - Utilities for the Python execution tests

### `test.support.script_helper` - Utilities for the Python execution tests

The `test.support.script_helper` module offers support for Python's script execution tests.

 test.support.script_helper.interpreter_requires_environment()

Yields `True` when `sys.executable interpreter` needs environment variables before it can run at all.

It is meant to pair with `@unittest.skipIf()` to mark tests that have to call an `assert_python*()` function in order to start an isolated-mode (`-I`) or no-environment-mode (`-E`) sub-interpreter process.

An ordinary build and test will not hit this case, but it may arise when one tries to run the standard library test suite from an interpreter lacking an obvious home under Python's present home-finding logic.

One approach to get the bulk of the testsuite running under such conditions is to set [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME). Other frequently seen environment variables that can affect whether the interpreter starts include [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) and `PYTHONUSERSITE`.

 test.support.script_helper.run_python_until_end(**args*, ***env_vars*)

Prepares the environment from *env_vars* in order to run the interpreter within a subprocess. Among the values allowed are `__isolated`, `__cleanenv`, `__cwd`, and `TERM`.

Changed in version 3.9: Whitespace is, as of this release, left intact on *stderr* by the function.

 test.support.script_helper.assert_python_ok(**args*, ***env_vars*)

Asserts that invoking the interpreter with *args* plus the optional environment variables *env_vars* succeeds (`rc == 0`), and returns a `(return code, stdout, stderr)` tuple.

When the *__cleanenv* keyword-only parameter is supplied, *env_vars* serves as a fresh environment.

Python launches in isolated mode (the command line option `-I`), unless the *__isolated* keyword-only parameter is set to `False`.

Changed in version 3.9: Whitespace is, as of this release, left intact on *stderr* by the function.

 test.support.script_helper.assert_python_failure(**args*, ***env_vars*)

Asserts that invoking the interpreter with *args* plus the optional environment variables *env_vars* fails (`rc != 0`), and returns a `(return code, stdout, stderr)` tuple.

Consult `assert_python_ok()` for additional options.

Changed in version 3.9: Whitespace is, as of this release, left intact on *stderr* by the function.

 test.support.script_helper.spawn_python(**args*, *stdout=subprocess.PIPE*, *stderr=subprocess.STDOUT*, ***kw*)

Launches a Python subprocess using the supplied arguments.

Here *kw* holds further keyword args forwarded to [`subprocess.Popen()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen). Returns a [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) object.

 test.support.script_helper.kill_python(*p*)

Lets the given [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) process run to the end and returns its stdout.

 test.support.script_helper.make_script(*script_dir*, *script_basename*, *source*, *omit_suffix=False*)

Writes a script holding *source* at the path made from *script_dir* and *script_basename*. When *omit_suffix* is `False`, `.py` is appended to the name. Returns the complete script path.

 test.support.script_helper.make_zip_script(*zip_dir*, *zip_basename*, *script_name*, *name_in_zip=None*)

Builds a zip file at *zip_dir* and *zip_basename* with the extension `zip`, holding the files from *script_name*. *name_in_zip* serves as the archive name. Returns a tuple holding `(full path, full path of archive name)`.

 test.support.script_helper.make_pkg(*pkg_dir*, *init_source=''*)

Builds a directory called *pkg_dir* that holds an `__init__` file whose contents are *init_source*.

 test.support.script_helper.make_zip_pkg(*zip_dir*, *zip_basename*, *pkg_name*, *script_basename*, *source*, *depth=1*, *compiled=False*)

Builds a zip package directory whose path comes from *zip_dir* and *zip_basename*, holding an empty `__init__` file plus a file *script_basename* whose contents are *source*. When *compiled* is `True`, both source files get compiled and placed into the zip package. Returns a tuple of the complete zip path together with the archive name of the zip file.

[Subject index](INDEX.md) · [Previous](../test-support-socket-helper/socket-test-network-availability-helpers.md) · [Continue](../test-support-bytecode-helper/test-support-bytecode-helper-bytecodetestcase-class.md)
