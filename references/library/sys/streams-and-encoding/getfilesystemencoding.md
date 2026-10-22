# sys.getfilesystemencoding

sys.getfilesystemencoding()

Fetch the [filesystem encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler): the encoding paired with the filesystem error handler when translating between Unicode filenames and bytes filenames. You obtain the filesystem error handler through `getfilesystemencodeerrors()`.

To maximize compatibility, prefer str for filenames everywhere, even though bytes filenames are supported too. Any function that takes or hands back filenames ought to handle both str and bytes, converting internally to whatever representation the system favors.

Rely on [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) and [`os.fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode) so that the proper encoding and errors mode are applied.

Python startup wires up the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) via the [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) function: refer to the [`filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) and [`filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) members of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

Changed in version 3.2: `getfilesystemencoding()` result cannot be `None` anymore.

Changed in version 3.6: On Windows, `'mbcs'` is no longer a guaranteed return value. Consult [**PEP 529**](https://peps.python.org/pep-0529/) along with `_enablelegacywindowsfsencoding()` for further detail.

Changed in version 3.7: Return `'utf-8'` if the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is enabled.

[API family](INDEX.md) · [sys context index](../INDEX.md).
