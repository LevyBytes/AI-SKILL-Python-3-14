# When to use logging

### When to use logging

To reach logging features, build a logger with `logger = logging.getLogger(__name__)`, then invoke that logger's [`debug()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.debug), [`info()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.info), [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.warning), [`error()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.error) and [`critical()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.critical) methods. For guidance on when logging fits, and on which logger method suits each case, consult the table that follows. For a range of frequent tasks, it names the tool that handles each task best.

| Task you want to perform | The best tool for the task |
| --- | --- |
| Show console output during everyday use of a program or command line script | `print()` |
| Note events arising while a program runs normally (for example, to monitor status or look into faults) | A logger’s `info()` (or `debug()` method for very detailed output for diagnostic purposes) |
| Issue a warning regarding a particular runtime event | `warnings.warn()` within library code when the problem can be avoided and the calling application ought to be changed so the warning goes away. A logger’s `warning()` method when nothing can be done by the calling application about the circumstance, yet the event deserves to be recorded |
| Report an error regarding a particular runtime event | Raise an exception |
| Note that an error was swallowed rather than raised as an exception (for instance, an error handler inside a long-running server process) | A logger’s `error()`, `exception()` or `critical()` method, whichever fits the particular error and the application's domain |

Each logger method draws its name from the level, or severity, of the events it is meant to record. Below are the built-in levels together with how they apply (listed from least to most severe):

| Level | When it’s used |
| --- | --- |
| `DEBUG` | Detailed information, typically of interest only when diagnosing problems. |
| `INFO` | Confirmation that things are working as expected. |
| `WARNING` | A sign that something out of the ordinary occurred, or that trouble may be coming soon (for example, ‘disk space low’). The software keeps running as expected. |
| `ERROR` | Owing to a more significant problem, the software could not carry out some function. |
| `CRITICAL` | A grave error, signaling that the program itself might not be able to keep running. |

Out of the box the level sits at `WARNING`, so only events at that severity or above get tracked, unless you configure the logging package differently.

There are several approaches to dealing with events once they are tracked. Printing them to the console is the most basic approach. Writing them out to a file on disk is another familiar approach.

[Subject index](INDEX.md) · [Previous source context](basic-logging-tutorial.md) · [Following source context](a-simple-example.md)
