# shlex - Improved Compatibility with Shells

### Improved Compatibility with Shells

Added in version 3.6.

The `shlex` class lines up with the parsing done by widespread Unix shells such as `bash`, `dash`, and `sh`. To tap into that alignment, pass the `punctuation_chars` argument to the constructor. Its `False` default keeps the pre-3.6 behaviour, but flip it to `True` and parsing of the characters `();<>|&` changes so that any run of them returns as a single token. This stops short of a complete shell parser (which the standard library wouldn't take on, given how many shells exist), yet it still lets you work through command lines with far less effort than otherwise. The snippet below shows the contrast:

```pycon
>>> import shlex
>>> text = "a && b; c && d || e; f >'abc'; (def \"ghi\")"
>>> s = shlex.shlex(text, posix=True)
>>> s.whitespace_split = True
>>> list(s)
['a', '&&', 'b;', 'c', '&&', 'd', '||', 'e;', 'f', '>abc;', '(def', 'ghi)']
>>> s = shlex.shlex(text, posix=True, punctuation_chars=True)
>>> s.whitespace_split = True
>>> list(s)
['a', '&&', 'b', ';', 'c', '&&', 'd', '||', 'e', ';', 'f', '>', 'abc', ';',
'(', 'def', 'ghi', ')']

```

Naturally, some returned tokens won't be valid for shells, so you will have to add your own error checking on the tokens you get back.

Rather than handing `True` to the punctuation_chars parameter, you may supply a string of particular characters, and those characters decide what counts as punctuation. As an example:

```python
>>> import shlex
>>> s = shlex.shlex("a && b || c", punctuation_chars="|")
>>> list(s)
['a', '&', '&', 'b', '||', 'c']

```

Note

Once `punctuation_chars` is given, the `wordchars` attribute gains the characters `~-./*?=`, since those characters show up in file names (wildcards included) and in command-line arguments (`--color=auto`, for one). Thus:

```python
>>> import shlex
>>> s = shlex.shlex('~/a && b-c --color=auto || d *.py?',
...                 punctuation_chars=True)
>>> list(s)
['~/a', '&&', 'b-c', '--color=auto', '||', 'd', '*.py?']

```

That said, for the closest possible match to the shell, the advice is to always pair `punctuation_chars` with `posix` and `whitespace_split`, which cancels out `wordchars` completely.

You'll get the best results setting `punctuation_chars` alongside `posix=True`. (Keep in mind that `shlex` defaults to `posix=False`.)

[Subject index](INDEX.md) · [Previous](parsing-rules.md) · [Owning module, declaration or section: shlex](shlex-split-to-shlex-join.md)
