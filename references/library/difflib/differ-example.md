# difflib - Differ example

Every sequence has to hold single-line strings that each end with a newline. The [`readlines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readlines) method of file-like objects yields exactly such sequences. The resulting delta is likewise made of newline-terminated strings, which can be printed directly through the [`writelines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.writelines) method of a file-like object.

### Differ example

Two texts are compared in this example. We begin by defining the texts as sequences of single-line strings that each end with a newline (the [`readlines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readlines) method of file-like objects can also yield such sequences):

```python
>>> text1 = '''  1. Beautiful is better than ugly.
...   2. Explicit is better than implicit.
...   3. Simple is better than complex.
...   4. Complex is better than complicated.
... '''.splitlines(keepends=True)
>>> len(text1)
4
>>> text1[0][-1]
'\n'
>>> text2 = '''  1. Beautiful is better than ugly.
...   3.   Simple is better than complex.
...   4. Complicated is better than complex.
...   5. Flat is better than nested.
... '''.splitlines(keepends=True)

```

Then we create a Differ object:

```python
>>> d = Differ()

```

Keep in mind that when creating a `Differ` object we can supply functions that strip out line and character “junk.” Consult the `Differ()` constructor for specifics.

Finally, we compare the two:

```python
>>> result = list(d.compare(text1, text2))

```

Since `result` is a list of strings, let’s pretty-print it:

```python
>>> from pprint import pprint
>>> pprint(result)
['    1. Beautiful is better than ugly.\n',
 '-   2. Explicit is better than implicit.\n',
 '-   3. Simple is better than complex.\n',
 '+   3.   Simple is better than complex.\n',
 '?     ++\n',
 '-   4. Complex is better than complicated.\n',
 '?            ^                     ---- ^\n',
 '+   4. Complicated is better than complex.\n',
 '?           ++++ ^                      ^\n',
 '+   5. Flat is better than nested.\n']

```

Rendered as one multi-line string, it appears like this:

```python
>>> import sys
>>> sys.stdout.writelines(result)
    1. Beautiful is better than ugly.
-   2. Explicit is better than implicit.
-   3. Simple is better than complex.
+   3.   Simple is better than complex.
?     ++
-   4. Complex is better than complicated.
?            ^                     ---- ^
+   4. Complicated is better than complex.
?           ++++ ^                      ^
+   5. Flat is better than nested.

```

[Subject index](INDEX.md) · [Continue](a-command-line-interface-to-difflib.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md) · [Owning module, declaration or section: difflib.Differ](difflib-differ-class.md) · [Owning module, declaration or section: Differ objects](difflib-differ-class.md) · [Owning module, declaration or section: compare](difflib-differ-compare.md) · [Preceding source contract and version conditions](difflib-differ-compare.md)
