# re - Exceptions

### Exceptions

 *exception *re.PatternError(*msg*, *pattern=None*, *pos=None*)

Raised whenever a string handed to one of the functions here is not a valid regular expression (perhaps it carries unmatched parentheses) or whenever some other failure crops up while compiling or matching. A string that holds no match for a pattern is never treated as an error. The `PatternError` instance carries these extra attributes:

 msg

The unformatted error message.

 pattern

The regular expression pattern.

 pos

The index in *pattern* where compilation failed (may be `None`).

 lineno

The line corresponding to *pos* (may be `None`).

 colno

The column corresponding to *pos* (may be `None`).

Changed in version 3.5: introduced the extra attributes.

Changed in version 3.13: `PatternError` started out under the name `error`; that older name survives as an alias for backward compatibility.

[Subject index](INDEX.md) · [Previous](re-escape-to-re-purge.md) · [Continue](re-pattern-class.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
