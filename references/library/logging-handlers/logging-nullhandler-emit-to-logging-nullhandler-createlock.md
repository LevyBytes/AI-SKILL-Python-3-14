# logging.handlers / NullHandler: `emit()`, `handle()`, `createLock()`

emit(*record*)

This method does nothing.

 handle(*record*)

This method does nothing.

 createLock()

This method hands back `None` for the lock, given that there's no underlying I/O whose access would have to be serialized.

Consult [Configuring Logging for a Library](https://docs.python.org/3.14/howto/logging.html#library-config) for further detail on putting `NullHandler` to use.

[Subject index](INDEX.md) · [Previous](logging-nullhandler-class.md) · [Continue](logging-handlers-watchedfilehandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.NullHandler](logging-nullhandler-class.md) · [Owning module, declaration or section: NullHandler](logging-nullhandler-class.md)
