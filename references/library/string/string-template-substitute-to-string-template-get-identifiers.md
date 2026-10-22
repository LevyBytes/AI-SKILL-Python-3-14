# string.Template: `substitute()`, `safe_substitute()`, `is_valid()`, `get_identifiers()`

substitute(*mapping={}*, */*, ***kwds*)

Carries out the template substitution and hands back a fresh string. Here *mapping* is any dictionary-like object whose keys line up with the template's placeholders. As an alternative, you can pass keyword arguments in which the keywords are the placeholders. When you supply both *mapping* and *kwds* and duplicates crop up, the placeholders from *kwds* win out.

 safe_substitute(*mapping={}*, */*, ***kwds*)

Behaves like `substitute()`, save that when placeholders are absent from *mapping* and *kwds*, rather than throwing a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception it leaves the original placeholder sitting untouched in the resulting string. On top of that, in contrast to `substitute()`, any further occurrences of the `$` merely yield `$` instead of throwing [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Even though other exceptions can still arise, this method earns the label "safe" because it always endeavors to hand back a usable string rather than throw an exception. Viewed another way, `safe_substitute()` could be anything but safe, given that it quietly overlooks malformed templates bearing dangling delimiters, unmatched braces, or placeholders that aren't valid Python identifiers.

 is_valid()

Gives back `False` whenever the template holds invalid placeholders that would drive `substitute()` to raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Added in version 3.11.

 get_identifiers()

Gives back a list of the template's valid identifiers, ordered by where each one first shows up, and passes over any invalid identifiers.

Added in version 3.11.

`Template` instances also provide one public data attribute:

[Subject index](INDEX.md) · [Previous](string-template-class.md) · [Continue](template-strings-strings.md) · [Owning module, declaration or section: string](string-common-string-operations.md) · [Owning module, declaration or section: string.Template](string-template-class.md) · [Owning module, declaration or section: Template strings ($-strings)](string-template-class.md)
