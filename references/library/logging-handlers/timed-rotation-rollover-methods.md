# logging.handlers.TimedRotatingFileHandler: `doRollover()`, `emit()`, `getFilesToDelete()`, `shouldRollover()`

doRollover()

Does a rollover, as described above.

 emit(*record*)

Outputs the record to the file, handling rollover in the manner described above.

 getFilesToDelete()

Hands back a list of filenames slated for removal during rollover. They are the absolute paths pointing at the oldest backup log files the handler wrote.

 shouldRollover(*record*)

See whether enough time has elapsed for a rollover to take place and, when it has, compute the next rollover time.

[Subject index](INDEX.md) · [Previous](logging-handlers-timedrotatingfilehandler-class.md) · [Continue](logging-handlers-sockethandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.TimedRotatingFileHandler](logging-handlers-timedrotatingfilehandler-class.md) · [Owning module, declaration or section: TimedRotatingFileHandler](logging-handlers-timedrotatingfilehandler-class.md)
