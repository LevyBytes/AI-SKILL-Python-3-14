# logging.handlers.WatchedFileHandler: `reopenIfNeeded()`, `emit()`

reopenIfNeeded()

Checks whether the file has changed. Should that be so, the current stream is flushed plus closed and the file reopened afresh, ordinarily as a prelude to outputting the record to the file.

Added in version 3.6.

 emit(*record*)

Outputs the record to the file, but first invokes `reopenIfNeeded()` to reopen the file should it have changed.

[Subject index](INDEX.md) · [Previous](logging-handlers-watchedfilehandler-class.md) · [Continue](logging-handlers-baserotatinghandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.WatchedFileHandler](logging-handlers-watchedfilehandler-class.md) · [Owning module, declaration or section: WatchedFileHandler](logging-handlers-watchedfilehandler-class.md)
