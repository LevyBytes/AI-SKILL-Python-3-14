# textwrap: `textwrap.TextWrapper`

*class *textwrap.TextWrapper(***kwargs*)

A range of optional keyword arguments is accepted by the `TextWrapper` constructor. Since each one maps to an instance attribute, for instance

```python
wrapper = TextWrapper(initial_indent="* ")

```

amounts to the same thing as

```python
wrapper = TextWrapper()
wrapper.initial_indent = "* "

```

The very same `TextWrapper` object can be reused as often as you like, and between uses you may tweak any of its settings by assigning straight to the instance attributes.

Here are the `TextWrapper` instance attributes (which double as the constructor’s keyword arguments):

 width

(default: `70`) The longest a wrapped line is allowed to be. Provided no single word in the input runs longer than `width`, `TextWrapper` promises that every output line stays within `width` characters.

 expand_tabs

(default: `True`) When true, every tab character in *text* is turned into spaces by way of the [`expandtabs()`](https://docs.python.org/3.14/library/stdtypes.html#str.expandtabs) method of *text*.

 tabsize

(default: `8`) When `expand_tabs` is true, each tab character in *text* becomes zero or more spaces, the count hinging on the present column and the tab size you specify.

Added in version 3.3.

 replace_whitespace

(default: `True`) When true, the `wrap()` method swaps each whitespace character for a single space — this happens once tabs are expanded but ahead of wrapping. The characters it swaps out are tab, newline, vertical tab, formfeed, and carriage return (`'\t\n\v\f\r'`).

Note

When `expand_tabs` is false while `replace_whitespace` is true, every tab character becomes one single space — and that is *not* the same thing as expanding tabs.

Note

When `replace_whitespace` is false, a newline can land mid-line and produce odd output. That’s why text ought to be broken into paragraphs (with [`str.splitlines()`](https://docs.python.org/3.14/library/stdtypes.html#str.splitlines) or the like) and each one wrapped on its own.

 drop_whitespace

(default: `True`) When true, whitespace sitting at the start and end of each line (once wrapping is done but before indenting) gets removed. That said, whitespace leading the paragraph survives if non-whitespace comes after it. Should the whitespace being removed fill a line entirely, that line is removed as a whole.

 initial_indent

(default: `''`) A string stuck onto the front of the first line of wrapped output. It is included in that first line’s length. An empty string adds no indentation.

 subsequent_indent

(default: `''`) A string stuck onto the front of every wrapped-output line apart from the first. It is included in the length of each such line, the first excepted.

 fix_sentence_endings

(default: `False`) When true, `TextWrapper` tries to spot where sentences end and makes sure two spaces, exactly, always sit between them. That’s usually what you want for monospaced-font text. The detection logic, though, isn’t flawless: it presumes a sentence finishes with a lowercase letter, then one of `'.'`, `'!'`, or `'?'`, optionally one of `'"'` or `"'"`, and finally a space. A snag with this scheme is that it can’t tell apart “Dr.” in

```python
[...] Dr. Frankenstein's monster [...]

```

from “Spot.” over in

```python
[...] See Spot. See Spot run [...]

```

By default `fix_sentence_endings` is false.

Because the sentence-spotting logic leans on `string.lowercase` to define a “lowercase letter” and on the habit of placing two spaces after a period to part sentences sharing a line, it applies specifically to English-language text.

 break_long_words

(default: `True`) When true, words running past `width` get split so that no line exceeds `width`. When false, long words stay intact and certain lines may run past `width`. (A long word is placed alone on its own line, keeping the amount by which `width` is overshot as small as possible.)

[Subject index](INDEX.md) · [Previous](textwrap-indent.md) · [Continue](textwrap-textwrapper-wrap-to-textwrap-textwrapper-fill.md) · [Owning module, declaration or section: textwrap](textwrap-wrap-to-textwrap-dedent.md)
