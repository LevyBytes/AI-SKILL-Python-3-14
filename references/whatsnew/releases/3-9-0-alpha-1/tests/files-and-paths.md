# Python 3.9.0 alpha 1 / tests / files and paths

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): test_distutils.test_build_ext() can now delete the temporary directory on Windows: rather than importing the freshly built C extension ("xx") within the current process, it exercises it inside a separated process.

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): test_winconsoleio stops leaking a temporary file: it uses tempfile.TemporaryFile() so the file disappears once the test finishes.

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): Repair test_shutil so it stops leaking temporary files.

[bpo-37359](https://bugs.python.org/issue?@action=redirect&bpo=37359): Provide a --cleanup option for python3 -m test that clears `test_python_*` directories from earlier failed jobs. Also add "make cleantest" to invoke `python3 -m test --cleanup`.

[bpo-38470](https://bugs.python.org/issue?@action=redirect&bpo=38470): Repair `test_compileall.test_compile_dir_maxlevels()` on Windows lacking long path support: build only 3 subdirectories rather than somewhere between 20 and 100 subdirectories.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
