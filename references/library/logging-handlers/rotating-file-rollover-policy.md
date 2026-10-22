# logging.handlers.RotatingFileHandler: `doRollover()`, `emit()`, `shouldRollover()`

doRollover()

Does a rollover, as described above.

 emit(*record*)

Outputs the record to the file, handling rollover in the manner described earlier.

 shouldRollover(*record*)

See whether the supplied record would push the file past the configured size limit.

[Subject index](INDEX.md) · [Previous](logging-handlers-rotatingfilehandler-class.md) · [Continue](logging-handlers-timedrotatingfilehandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.RotatingFileHandler](logging-handlers-rotatingfilehandler-class.md) · [Owning module, declaration or section: RotatingFileHandler](logging-handlers-rotatingfilehandler-class.md)
