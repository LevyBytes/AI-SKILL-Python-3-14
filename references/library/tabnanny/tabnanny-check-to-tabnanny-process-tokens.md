# tabnanny — `tabnanny` — Detection of ambiguous indentation

## tabnanny — Detection of ambiguous indentation

### `tabnanny` — Detection of ambiguous indentation

**Source code:** [Lib/tabnanny.py](https://github.com/python/cpython/tree/3.14/Lib/tabnanny.py)

---

For now this module is meant to be run as a script. That said, you can import it into an IDE and call on the `check()` function covered below.

Note

The API this module exposes is apt to shift in upcoming releases, and those shifts may break backward compatibility.

 tabnanny.check(*file_or_dir*)

When *file_or_dir* names a directory rather than a symbolic link, the function walks the directory tree under *file_or_dir* recursively, inspecting every `.py` file it meets. When *file_or_dir* is a plain Python source file instead, it gets examined for whitespace-related trouble. Diagnostic messages go to standard output by way of the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function.

 tabnanny.verbose

A flag governing whether verbose messages are printed. Running as a script bumps it up via the `-v` option.

 tabnanny.filename_only

A flag governing whether only the names of files with whitespace-related trouble get printed. Running as a script turns it true via the `-q` option.

 *exception *tabnanny.NannyNag

Thrown by `process_tokens()` upon spotting an ambiguous indent. It is caught and dealt with inside `check()`.

 tabnanny.process_tokens(*tokens*)

`check()` calls on this function to work through the tokens that the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module produces.

See also

Module [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize)

A lexical scanner for Python source code.

[Subject index](INDEX.md)
