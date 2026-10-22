# logging.handlers / FileHandler: `close()`, `emit()`

close()

Closes the file.

 emit(*record*)

Outputs the record to the file.

Be aware that should the file have been closed because of logging shutdown at exit, with the file mode being 'w', the record won't be emitted (see [bpo-42378](https://bugs.python.org/issue?@action=redirect&bpo=42378)).

[Subject index](INDEX.md) · [Previous](logging-filehandler-class.md) · [Continue](logging-nullhandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.FileHandler](logging-filehandler-class.md) · [Owning module, declaration or section: FileHandler](logging-filehandler-class.md)
