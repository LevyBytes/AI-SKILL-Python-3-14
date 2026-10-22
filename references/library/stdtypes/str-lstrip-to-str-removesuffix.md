# stdtypes: `str.lstrip()`, `str.partition()`, `str.removeprefix()`, `str.removesuffix()`

str.lstrip(*chars=None*, */*)

Yields a copy of the string from which leading characters have been dropped. The *chars* argument is a string naming the collection of characters to drop. When left out or set to `None`, the *chars* argument falls back to dropping whitespace. The *chars* argument is not treated as a prefix; instead, each combination of its members gets stripped:

```python
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'

```

Refer to `str.removeprefix()` for a method that drops one single prefix string in place of any character drawn from a set. Consider this:

```python
>>> 'Arthur: three!'.lstrip('Arthur: ')
'ee!'
>>> 'Arthur: three!'.removeprefix('Arthur: ')
'three!'

```

 *static *str.maketrans(*dict*, */*)

 *static *str.maketrans(*from*, *to*, *remove=''*, */*)

This static method yields a translation table that `str.translate()` can use.

When called with a single argument, that argument is required to be a dictionary whose keys are Unicode ordinals (integers) or single-character strings (strings of length 1) and whose values are Unicode ordinals, strings (of any length) or `None`. Keys that are characters then get turned into ordinals.

When called with two arguments, both have to be strings of identical length, and within the resulting dictionary each character of *from* is mapped onto the character occupying the matching position in *to*. A third argument, if supplied, has to be a string whose characters become mapped to `None` in the outcome.

 str.partition(*sep*, */*)

Divides the string at the earliest occurrence of *sep*, returning a 3-tuple made up of the portion ahead of the separator, the separator itself, and the portion after it. When the separator is absent, returns a 3-tuple holding the string itself followed by two empty strings.

Consider this:

```pycon
>>> 'Monty Python'.partition(' ')
('Monty', ' ', 'Python')
>>> "Monty Python's Flying Circus".partition(' ')
('Monty', ' ', "Python's Flying Circus")
>>> 'Monty Python'.partition('-')
('Monty Python', '', '')

```

See also `rpartition()`.

 str.removeprefix(*prefix*, */*)

When the string begins with the *prefix* string, returns `string[len(prefix):]`. In every other case, returns a copy of the original string:

```pycon
>>> 'TestHook'.removeprefix('Test')
'Hook'
>>> 'BaseTestCase'.removeprefix('Test')
'BaseTestCase'

```

Added in version 3.9.

See also `removesuffix()` and `startswith()`.

 str.removesuffix(*suffix*, */*)

When the string finishes with the *suffix* string and that *suffix* is non-empty, returns `string[:-len(suffix)]`. In every other case, returns a copy of the original string:

```pycon
>>> 'MiscTests'.removesuffix('Tests')
'Misc'
>>> 'TmpDirMixin'.removesuffix('Tests')
'TmpDirMixin'

```

Added in version 3.9.

See also `removeprefix()` and `endswith()`.

[Subject index](INDEX.md) · [Previous](str-istitle-to-str-lower.md) · [Continue](str-replace-to-str-rpartition.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
