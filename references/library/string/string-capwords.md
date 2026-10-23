# string - Helper functions

### Helper functions

 string.capwords(*s*, *sep=None*)

Breaks the argument into words via [`str.split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split), capitalizes each one via [`str.capitalize()`](https://docs.python.org/3.14/library/stdtypes.html#str.capitalize), and rejoins the capitalized words via [`str.join()`](https://docs.python.org/3.14/library/stdtypes.html#str.join). Where the optional second argument *sep* is missing or `None`, stretches of whitespace characters collapse to a single space and any leading or trailing whitespace is stripped; otherwise *sep* drives both the splitting and the rejoining of the words.

[Subject index](INDEX.md) · [Previous](template-strings-strings.md) · [Owning module, declaration or section: string](string-common-string-operations.md)
