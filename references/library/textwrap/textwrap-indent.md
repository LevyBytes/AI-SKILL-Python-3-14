# textwrap: `textwrap.indent()`

textwrap.indent(*text*, *prefix*, *predicate=None*)

Tack *prefix* onto the front of chosen lines within *text*.

Splitting into lines happens via a call to `text.splitlines(True)`.

Out of the box, *prefix* goes onto every line that is not made up entirely of whitespace (line endings counted in).

For example:

```python
>>> s = 'hello\n\n \nworld'
>>> indent(s, '  ')
'  hello\n\n \n  world'

```

You can steer which lines get indented through the optional *predicate* argument. As a case in point, it’s trivial to attach *prefix* even to empty and whitespace-only lines:

```python
>>> print(indent(s, '+ ', lambda line: True))
+ hello
+
+
+ world

```

Added in version 3.3.

Under the hood, `wrap()`, `fill()` and `shorten()` each spin up a `TextWrapper` instance and invoke one method on it. Because that instance gets thrown away afterward, programs that push lots of strings through `wrap()` and/or `fill()` may run faster if you build and keep your own `TextWrapper` object.

The wrapper favors breaking at whitespace and just past the hyphens of hyphenated words; only after that will it split long words when it has to, unless you set `TextWrapper.break_long_words` to false.

[Subject index](INDEX.md) · [Previous](textwrap-wrap-to-textwrap-dedent.md) · [Continue](textwrap-textwrapper-class.md) · [Owning module, declaration or section: textwrap](textwrap-wrap-to-textwrap-dedent.md)
