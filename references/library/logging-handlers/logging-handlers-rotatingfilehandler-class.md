# logging.handlers: `logging.handlers.RotatingFileHandler`

### RotatingFileHandler

Found in the `logging.handlers` module, the `RotatingFileHandler` class supports rotation of disk log files.

 `*class *logging.handlers.RotatingFileHandler(*filename*, *mode='a'*, *maxBytes=0*, *backupCount=0*, *encoding=None*, *delay=False*, *errors=None*)`

Hands back a fresh instance of the `RotatingFileHandler` class. The named file is opened and serves as the stream for logging. When *mode* is left unspecified, `'a'` applies. When *encoding* is not `None`, it governs opening the file with that encoding. When *delay* is true, opening the file is held off until `emit()` is first called. The file, by default, keeps growing without bound. When *errors* is provided, it decides how encoding errors get handled.

The *maxBytes* and *backupCount* values let you have the file *rollover* at a preset size. As the size is on the verge of being passed, the file is closed and a fresh file is silently opened for output. Rollover takes place whenever the current log file approaches *maxBytes* in length; but should either *maxBytes* or *backupCount* be zero, rollover never happens, so as a rule you'll want *backupCount* at 1 or more along with a non-zero *maxBytes*. With a non-zero *backupCount*, the system keeps old log files by tacking the extensions '.1', '.2' etc. onto the filename. To illustrate, given a *backupCount* set to 5 plus a base file name of `app.log`, you'd wind up with `app.log`, `app.log.1`, `app.log.2`, on up to `app.log.5`. The file currently being written is forever `app.log`. Once this file fills up, it gets closed and renamed to `app.log.1`, and if files `app.log.1`, `app.log.2`, etc. already exist, then they get renamed to `app.log.2`, `app.log.3` etc. respectively.

Changed in version 3.6: Beyond string values, [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects are now accepted too for the *filename* argument.

Changed in version 3.9: The *errors* parameter was added.

[Subject index](INDEX.md) · [Previous](base-handler-rotation-name-and-operation.md) · [Continue](rotating-file-rollover-policy.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
