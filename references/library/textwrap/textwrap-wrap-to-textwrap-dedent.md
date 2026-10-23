# textwrap: `textwrap.wrap()`, `textwrap.fill()`, `textwrap.shorten()`, `textwrap.dedent()`

## textwrap - Text wrapping and filling

### `textwrap` - Text wrapping and filling

**Source code:** [Lib/textwrap.py](https://github.com/python/cpython/tree/3.14/Lib/textwrap.py)

---

Alongside a handful of convenience functions, the `textwrap` module ships `TextWrapper`, the class where the real work happens. For wrapping or filling just a string or two, those convenience functions will do fine; beyond that, lean on a `TextWrapper` instance for the sake of efficiency.

`textwrap.wrap(*text*, *width=70*, ***, *initial_indent=''*, *subsequent_indent=''*, *expand_tabs=True*, *replace_whitespace=True*, *fix_sentence_endings=False*, *break_long_words=True*, *drop_whitespace=True*, *break_on_hyphens=True*, *tabsize=8*, *max_lines=None*, *placeholder=' [...]'*)`

Takes the lone paragraph held in *text* (a string) and breaks it so no line runs past *width* characters. Hands back a list of the resulting lines, each lacking a trailing newline.

The optional keyword arguments map onto the `TextWrapper` instance attributes that are described further down.

For more on how `wrap()` behaves, look at the `TextWrapper.wrap()` method.

`textwrap.fill(*text*, *width=70*, ***, *initial_indent=''*, *subsequent_indent=''*, *expand_tabs=True*, *replace_whitespace=True*, *fix_sentence_endings=False*, *break_long_words=True*, *drop_whitespace=True*, *break_on_hyphens=True*, *tabsize=8*, *max_lines=None*, *placeholder=' [...]'*)`

Breaks the one paragraph in *text* and gives back a single string holding the wrapped paragraph. In effect, `fill()` is just a shorthand for

```python
"\n".join(wrap(text, ...))

```

Notably, the keyword arguments `fill()` takes are precisely those of `wrap()`.

 textwrap.shorten(*text*, *width*, ***, *fix_sentence_endings=False*, *break_long_words=True*, *break_on_hyphens=True*, *placeholder=' [...]'*)

Squeeze and trim the supplied *text* so it sits inside the supplied *width*.

To begin, the whitespace within *text* is squeezed down (every run of whitespace becomes one space). Should the outcome sit inside the *width*, that is what comes back. If not, words are shed off the tail end until what’s left, together with the *placeholder*, fits inside *width*:

```python
>>> textwrap.shorten("Hello  world!", width=12)
'Hello world!'
>>> textwrap.shorten("Hello  world!", width=11)
'Hello [...]'
>>> textwrap.shorten("Hello world", width=10, placeholder="...")
'Hello...'

```

The optional keyword arguments line up with the `TextWrapper` instance attributes detailed below. Bear in mind the whitespace is squeezed before the text ever reaches the `TextWrapper` `fill()` function, which means adjusting `tabsize`, `expand_tabs`, `drop_whitespace`, and `replace_whitespace` does nothing here.

Added in version 3.4.

 textwrap.dedent(*text*)

Strip whatever leading whitespace is shared by all lines of *text*.

A handy use is making triple-quoted strings sit flush against the display’s left margin while still keeping them indented within the source code itself.

Keep in mind that, although tabs and spaces both count as whitespace, they are not interchangeable: the lines `" hello"` and `"\thello"` are taken to share no common leading whitespace.

Any line made up purely of whitespace is skipped on input and reduced to a lone newline character on output.

For example:

```python
def test():
    # end first line with \ to avoid the empty line!
    s = '''\
    hello
      world
    '''
    print(repr(s))          # prints '    hello\n      world\n    '
    print(repr(dedent(s)))  # prints 'hello\n  world\n'

```

Changed in version 3.14: The `dedent()` function now properly normalizes blank lines made up solely of whitespace characters. Before this, it only normalized blank lines built from tabs and spaces.

[Subject index](INDEX.md) · [Continue](textwrap-indent.md)
