# logging / Formatter Objects: `logging.BufferingFormatter`, `formatHeader()`, `formatFooter()`, `format()`

*class *logging.BufferingFormatter(*linefmt=None*)

A base formatter class fit for subclassing whenever you wish to format a batch of records. You can hand it a `Formatter` instance to use for formatting each line (which corresponds to a single record). Where none is supplied, the default formatter (which merely outputs the event message) serves as the line formatter.

 formatHeader(*records*)

Return a header for a list of *records*. The base implementation merely returns the empty string. To get particular behaviour you will have to override this method, e.g. so as to show how many records there are, a title or a separator line.

 formatFooter(*records*)

Return a footer for a list of *records*. The base implementation merely returns the empty string. To get particular behaviour you will have to override this method, e.g. so as to show how many records there are or a separator line.

 format(*records*)

Return formatted text for a list of *records*. The base implementation merely returns the empty string when there are no records; otherwise, it returns the header, each record formatted by the line formatter, and the footer all concatenated together.

[Subject index](INDEX.md) · [Previous](logging-formatter-format-to-logging-formatter-formatstack.md) · [Continue](logging-filter-class.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: Formatter Objects](logging-formatter-class.md)
