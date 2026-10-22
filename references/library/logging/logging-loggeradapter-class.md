# logging: `logging.LoggerAdapter`

### LoggerAdapter Objects

`LoggerAdapter` instances offer a convenient way to feed contextual information into logging calls. For a usage example, turn to the section on [adding contextual information to your logging output](https://docs.python.org/3.14/howto/logging-cookbook.html#context-info).

 *class *logging.LoggerAdapter(*logger*, *extra=None*, *merge_extra=False*)

Returns a `LoggerAdapter` instance initialized with an underlying `Logger` instance, an optional dict-like object (*extra*), plus an optional boolean (*merge_extra*) that signals whether the *extra* argument of individual log calls ought to be merged with the `LoggerAdapter` extra. By default the behavior overlooks the *extra* argument of individual log calls and draws solely on the one belonging to the `LoggerAdapter` instance

[Subject index](INDEX.md) · [Previous](logrecord-attributes.md) · [Continue](logging-loggeradapter-process.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
