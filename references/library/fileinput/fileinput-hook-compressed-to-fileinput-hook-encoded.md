# fileinput: `fileinput.hook_compressed()`, `fileinput.hook_encoded()`

fileinput.hook_compressed(*filename*, *mode*, ***, *encoding=None*, *errors=None*)

Opens gzip- and bzip2-compressed files without any fuss — they are spotted by their `'.gz'` and `'.bz2'` extensions — by way of the [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) and [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) modules. Where the extension is neither `'.gz'` nor `'.bz2'`, the file opens the ordinary way (that is, through [`open()`](https://docs.python.org/3.14/library/functions.html#open) with no decompression applied).

For compressed files the `encoding` and `errors` values go to [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper), whereas for ordinary files they go to open.

Usage example: `fi = fileinput.FileInput(openhook=fileinput.hook_compressed, encoding="utf-8")`

Changed in version 3.10: Picked up the keyword-only `encoding` and `errors` parameters.

 fileinput.hook_encoded(*encoding*, *errors=None*)

Yields a hook that opens every file through [`open()`](https://docs.python.org/3.14/library/functions.html#open), reading it with the `encoding` and `errors` you provide.

Usage example: `fi = fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8", "surrogateescape"))`

Changed in version 3.6: Added the optional *errors* parameter.

Deprecated since version 3.10: With `fileinput.input()` and `FileInput` now carrying their own `encoding` and `errors` parameters, this function is on its way out.

[Subject index](INDEX.md) · [Previous](fileinput-fileinput-class.md) · [Continue](../filesys/file-and-directory-access.md) · [Owning module, declaration or section: fileinput](fileinput-input-to-fileinput-nextfile.md)
