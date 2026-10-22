# tempfile: `tempfile.gettempdirb()`, `tempfile.gettempprefix()`, `tempfile.gettempprefixb()`, `tempfile.tempdir`

tempfile.gettempdirb()

Behaves like `gettempdir()`, only the value returned is in bytes.

Added in version 3.5.

 tempfile.gettempprefix()

Hands back the filename prefix applied when temporary files are created. The directory part is not included.

 tempfile.gettempprefixb()

Behaves like `gettempprefix()`, only the value returned is in bytes.

Added in version 3.5.

To hold the name of the temporary-file directory that `gettempdir()` reports, the module keeps a global variable. You can assign to it directly to bypass the selection process, though doing so is discouraged. Every function in this module accepts a *dir* argument for naming the directory; that is the recommended route, and it avoids catching other unsuspecting code off guard by mutating global API behavior.

 tempfile.tempdir

Once given a value that isn't `None`, this variable sets the default for the *dir* argument across the functions this module defines, type included — bytes or str. It is not allowed to be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Should `tempdir` be `None` (its default) when any of the above functions other than `gettempprefix()` is called, it gets initialized by the algorithm laid out in `gettempdir()`.

Note

Watch out: assigning `tempdir` a bytes value brings an unpleasant side effect. The global default return type of `mkstemp()` and `mkdtemp()` flips to bytes whenever no explicit `prefix`, `suffix`, or `dir` argument of type str is given. Do not write code that counts on this. The clumsy behavior survives only to stay compatible with how things historically worked.

[Subject index](INDEX.md) · [Previous](tempfile-mkstemp-to-tempfile-gettempdir.md) · [Continue](examples.md) · [Owning module, declaration or section: tempfile](tempfile-generate-temporary-files-and-directories.md)
