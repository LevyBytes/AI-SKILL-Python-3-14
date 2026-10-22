# logging: `logging.Formatter`

### Formatter Objects

 `*class *logging.Formatter(*fmt=None*, *datefmt=None*, *style='%'*, *validate=True*, ***, *defaults=None*)`

Charged with turning a `LogRecord` into an output string meant for a human or external system to read.

Parameters:

- **fmt** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – A format string in the given *style* covering the logged output as a whole. The available mapping keys come from the `LogRecord` object's LogRecord attributes. When left unspecified, `'%(message)s'` applies, which is simply the logged message.

- **datefmt** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – A format string covering the date/time piece of the logged output. When left unspecified, the default spelled out in `formatTime()` applies.

-

[Subject index](INDEX.md) · [Previous](logging-handler-createlock-to-logging-handler-emit.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Required continuation of the source contract](logging-formatter-constructor-and-methods.md)
