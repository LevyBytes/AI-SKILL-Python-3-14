# 2.2.1. Source Code Encoding

### 2.2. The Interpreter and Its Environment

### 2.2.1. Source Code Encoding

Out of the box, Python regards source files as being encoded in UTF-8. Under that encoding, characters from nearly every language on earth may appear together within string literals, identifiers, and comments — though the standard library sticks to ASCII characters for its identifiers, a convention worth following in any portable code. For these characters to render correctly, your editor has to recognize the file as UTF-8 and rely on a font that covers every character the file holds.

To announce an encoding apart from the default, place a special comment line as the *first* line of the file. Its syntax goes like this:

```python
# -*- coding: encoding -*-

```

in which *encoding* names one of the legitimate [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) that Python supports.

As an instance, to state that Windows-1252 encoding applies, the opening line of your source code file ought to read:

```python
# -*- coding: cp1252 -*-

```

The *first line* rule has one exception: when the source code opens with a [UNIX “shebang” line](https://docs.python.org/3.14/tutorial/appendix.html#tut-scripts). Here the encoding declaration belongs on the file's second line instead. For example:

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-

```

Footnotes

[Subject index](INDEX.md) · [Previous source section](interactive-mode.md)
