# logging.handlers: `logging.FileHandler`

### FileHandler

Found in the core [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package, the `FileHandler` class routes logging output to a disk file. From `StreamHandler` it inherits the output functionality.

 *class *logging.FileHandler(*filename*, *mode='a'*, *encoding=None*, *delay=False*, *errors=None*)

Hands back a fresh instance of the `FileHandler` class. The named file is opened and serves as the stream for logging. When *mode* is left unspecified, `'a'` applies. When *encoding* is not `None`, it governs opening the file with that encoding. When *delay* is true, opening the file is held off until `emit()` is first called. The file, by default, keeps growing without bound. When *errors* is given, it decides how encoding errors get handled.

Changed in version 3.6: Beyond string values, [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects are now accepted too for the *filename* argument.

Changed in version 3.9: The *errors* parameter was added.

[Subject index](INDEX.md) · [Previous](logging-streamhandler-emit-to-logging-streamhandler-setstream.md) · [Continue](logging-filehandler-close-to-logging-filehandler-emit.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
