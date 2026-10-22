# textwrap.TextWrapper: `wrap()`, `fill()`

break_on_hyphens

(default: `True`) When true, breaks are taken by preference at whitespace and immediately after hyphens inside compound words, following English custom. When false, only whitespace counts as a candidate spot for a line break, yet you must set `break_long_words` to false to get genuinely insecable words. Earlier versions defaulted to permitting hyphenated words to be broken at all times.

 max_lines

(default: `None`) Unless set to `None`, the output holds no more than *max_lines* lines, with *placeholder* tacked on at the very end.

Added in version 3.4.

 placeholder

(default: `' [...]'`) A string shown at the close of the output text whenever that text has been truncated.

Added in version 3.4.

Beyond the attributes, `TextWrapper` exposes a few public methods that mirror the module-level convenience functions:

 wrap(*text*)

Takes the lone paragraph held in *text* (a string) and breaks it so each line runs no more than `width` characters. Every wrapping option is pulled from the `TextWrapper` instance’s own attributes. Hands back a list of output lines, each without a trailing newline. When the wrapped output holds nothing, the list returned is empty.

 fill(*text*)

Breaks the one paragraph in *text* and gives back a single string holding the wrapped result.

[Subject index](INDEX.md) · [Previous](textwrap-textwrapper-class.md) · [Owning module, declaration or section: textwrap](textwrap-wrap-to-textwrap-dedent.md) · [Owning module, declaration or section: textwrap.TextWrapper](textwrap-textwrapper-class.md)
