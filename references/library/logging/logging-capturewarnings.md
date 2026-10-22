# logging — Integration with the warnings module

### Integration with the warnings module

You can employ the `captureWarnings()` function to weave `logging` together with the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module.

 logging.captureWarnings(*capture*)

This function serves to switch logging's capture of warnings on or off.

Where *capture* is `True`, warnings raised by the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module get rerouted into the logging system. To be specific, a warning gets formatted via [`warnings.formatwarning()`](https://docs.python.org/3.14/library/warnings.html#warnings.formatwarning) and the resulting string is logged to a logger named `'py.warnings'` at a severity of `WARNING`.

Where *capture* is `False`, the rerouting of warnings into the logging system ceases, and warnings revert to their original destinations (namely those in force prior to `captureWarnings(True)` being called).

See also

Module [`logging.config`](https://docs.python.org/3.14/library/logging.config.html#module-logging.config)

Configuration API for the logging module.

Module [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers)

Useful handlers included with the logging module.

[**PEP 282**](https://peps.python.org/pep-0282/) - A Logging System

The proposal that laid out this capability for adoption into Python's standard library.

[Original Python logging package](https://old.red-dove.com/python_logging.html)

This is the original source for the `logging` package. The release of the package offered from this site works with Python 1.5.2, 2.1.x and 2.2.x, none of which bundle the `logging` package within the standard library.

[Subject index](INDEX.md) · [Previous](logging-lastresort-to-logging-raiseexceptions.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
