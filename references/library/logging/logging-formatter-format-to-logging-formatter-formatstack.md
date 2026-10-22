# logging.Formatter: `format()`, `formatTime()`, `formatException()`, `formatStack()`

format(*record*)

A string formatting operation takes the record's attribute dictionary as its operand. Returns the resulting string. A couple of preparatory steps run before the dictionary is formatted. The record's *message* attribute is computed from *msg* % *args*. Should the formatting string contain `'(asctime)'`, `formatTime()` is called to format the event time. Where exception information exists, `formatException()` formats it and it is appended to the message. Note that attribute *exc_text* caches the formatted exception information. This proves handy because the exception information can be pickled and sent across the wire, yet you should take care when you have more than one `Formatter` subclass that customizes the formatting of exception information. Under that circumstance, you will have to clear the cached value (by setting the *exc_text* attribute to `None`) once a formatter has finished its formatting, so that the next formatter handling the event does not reuse the cached value but recomputes it from scratch.

Where stack information is available, it is appended after the exception information, with `formatStack()` transforming it where needed.

 formatTime(*record*, *datefmt=None*)

A formatter that wishes to use a formatted time should call this method from [`format()`](https://docs.python.org/3.14/library/functions.html#format). You can override this method in formatters to meet any particular requirement, but the basic behavior runs as follows: when *datefmt* (a string) is supplied, it is paired with [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) to format the record's creation time. Otherwise, the format "%Y-%m-%d %H:%M:%S,uuu" applies, where the uuu part is a millisecond value and the remaining letters follow the `time.strftime()` documentation. One example time in this format is `2003-01-23 00:29:50,411`. The resulting string is returned.

A user-configurable function is used by this function to convert the creation time into a tuple. The default is [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime); to alter this for a particular formatter instance, set the `converter` attribute to a function whose signature matches `time.localtime()` or [`time.gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime). To alter it for every formatter, for instance if you want all logging times shown in GMT, set the `converter` attribute on the `Formatter` class.

Changed in version 3.3: Formerly, the default format sat hard-coded much like this example: `2010-09-06 22:38:15,292`, where a strptime format string (`'%Y-%m-%d %H:%M:%S'`) handles the portion ahead of the comma, while the portion after the comma is a millisecond value. Since strptime offers no format placeholder for milliseconds, that millisecond value is tacked on through a second format string, `'%s,%03d'` — and both of those format strings used to be hardcoded into this method. After the change, these strings now live as class-level attributes that you can override at the instance level whenever you wish. Those attributes go by the names `default_time_format` (for the strptime format string) and `default_msec_format` (for appending the millisecond value).

Changed in version 3.9: The `default_msec_format` can be `None`.

 formatException(*exc_info*)

Formats the given exception information (a standard exception tuple such as [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns) into a string. This default implementation merely uses [`traceback.print_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_exception). The resulting string is returned.

 formatStack(*stack_info*)

Formats the given stack information (a string such as [`traceback.print_stack()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_stack) returns, only with the final newline stripped) into a string. This default implementation merely returns the input value.

[Subject index](INDEX.md) · [Previous](logging-formatter-constructor-and-methods.md) · [Continue](buffering-formatter-class-and-format.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Formatter](logging-formatter-class.md) · [Owning module, declaration or section: Formatter Objects](logging-formatter-class.md)
