# logging.handlers: `logging.handlers.WatchedFileHandler`

### WatchedFileHandler

Found in the `logging.handlers` module, the `WatchedFileHandler` class is a `FileHandler` that keeps an eye on the file it logs to. Whenever the file changes, it gets closed and reopened by the file name.

A file change may arise from the use of programs like *newsyslog* and *logrotate*, which carry out log file rotation. Designed for Unix/Linux use, this handler watches the file to detect whether it has changed since the prior emit. (A file counts as changed if its device or inode have changed.) Once a change is detected, the prior file stream gets closed, and the file is opened so a new stream can be obtained.

This handler is unsuitable for Windows use, since on Windows open log files can be neither moved nor renamed — logging opens the files with exclusive locks — so no such handler is called for. What's more, Windows offers no support for *ST_INO*; [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat) consistently returns zero for that value.

 `*class *logging.handlers.WatchedFileHandler(*filename*, *mode='a'*, *encoding=None*, *delay=False*, *errors=None*)`

Hands back a fresh instance of the `WatchedFileHandler` class. The named file is opened and serves as the stream for logging. When *mode* is left unspecified, `'a'` applies. When *encoding* is not `None`, it governs opening the file with that encoding. When *delay* is true, opening the file is held off until `emit()` is first called. The file, by default, keeps growing without bound. When *errors* is provided, it decides how encoding errors get handled.

Changed in version 3.6: Beyond string values, [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects are now accepted too for the *filename* argument.

Changed in version 3.9: The *errors* parameter was added.

[Subject index](INDEX.md) · [Previous](logging-nullhandler-emit-to-logging-nullhandler-createlock.md) · [Continue](watched-file-reopen-and-emission.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
