# logging — Logging Levels

### Logging Levels

The table below gives the numeric values of logging levels. These chiefly matter when you want to define your own levels and need them to hold particular values relative to the predefined ones. When you define a level sharing a numeric value, it overwrites the predefined value; the predefined name is lost.

| Level | Numeric value | What it means / When to use it |
| --- | --- | --- |
| logging.NOTSET | 0 | Placed on a logger, this signals that ancestor loggers should be checked to work out the effective level. Should that still come out to `NOTSET`, then every event is logged. Placed on a handler, every event is handled. |
| logging.DEBUG | 10 | Fine-grained detail, ordinarily useful only to a developer working to diagnose a problem. |
| logging.INFO | 20 | Confirmation that things are working as expected. |
| logging.WARNING | 30 | A sign that something unexpected took place, or that trouble may be coming soon (e.g. ‘disk space low’). The software keeps running as expected. |
| logging.ERROR | 40 | Owing to a graver problem, the software has been unable to carry out some function. |
| logging.CRITICAL | 50 | A grave error, signalling that the program itself may not be able to keep running. |

[Subject index](INDEX.md) · [Previous](logging-logger-addfilter-to-logging-logger-hashandlers.md) · [Continue](logging-handler-class-to-init.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
