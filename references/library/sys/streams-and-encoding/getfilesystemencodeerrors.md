# sys.getfilesystemencodeerrors

sys.getfilesystemencodeerrors()

Fetch the [filesystem error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler): the error handler paired with the filesystem encoding when translating between Unicode filenames and bytes filenames. You obtain the filesystem encoding through `getfilesystemencoding()`.

Rely on [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) and [`os.fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode) so that the proper encoding and errors mode are applied.

Python startup wires up the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) via the [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) function: refer to the [`filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) and [`filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) members of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

Added in version 3.6.

[API family](INDEX.md) · [sys context index](../INDEX.md).
