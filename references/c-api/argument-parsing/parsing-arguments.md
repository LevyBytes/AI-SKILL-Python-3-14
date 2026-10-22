# Parsing arguments

### Parsing arguments

Any format string is built from zero or more “format units.” Each format unit stands for one Python object; typically it is a lone character or a parenthesized run of format units. Apart from a handful of exceptions, a format unit that is not a parenthesized run usually maps to one address argument supplied to these functions. Throughout the description below, the quoted item is the format unit; the entry in (round) parentheses is the matching Python object type; and the entry in [square] brackets gives the type of the C variable(s) whose address you must hand over.

[Subject index](INDEX.md) · [Previous source contract](parsing-arguments-and-building-values.md) · [Following source contract](string-buffer-memory-ownership.md)
