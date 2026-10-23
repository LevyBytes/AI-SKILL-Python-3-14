# References

### References

The [Unicode Consortium site](https://www.unicode.org) offers character charts, a glossary, and PDF editions of the Unicode specification. Expect some heavy reading. The site also provides [A chronology](https://www.unicode.org/history/) tracing the origin and evolution of Unicode.

Over on the Computerphile Youtube channel, Tom Scott offers a short talk where he [discusses the history of Unicode and UTF-8](https://www.youtube.com/watch?v=MijmeoH9LT4) (9 minutes 36 seconds).

As an aid to grasping the standard, Jukka Korpela has produced [an introductory guide](https://jkorpela.fi/unicode/guide.html) on how to read the Unicode character tables.

There is another [good introductory article](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) by Joel Spolsky. Should this introduction have left things murky, give that alternate article a read before you go on.

Entries on Wikipedia tend to be useful; consult the entries for “[character encoding](https://en.wikipedia.org/wiki/Character_encoding)” and [UTF-8](https://en.wikipedia.org/wiki/UTF-8), as examples.

### References

A few worthwhile alternative treatments of Python’s Unicode support are:

- [Processing Text Files in Python 3](https://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html), by Nick Coghlan.

- [Pragmatic Unicode](https://nedbatchelder.com/text/unipain.html), a PyCon 2012 presentation by Ned Batchelder.

A description of the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type lives in the Python library reference at [Text Sequence Type - str](https://docs.python.org/3.14/library/stdtypes.html#textseq).

The documentation for the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module.

The documentation for the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module.

Marc-André Lemburg delivered [a presentation titled “Python and Unicode” (PDF slides)](https://downloads.egenix.com/python/Unicode-EPC2002-Talk.pdf) at EuroPython 2002. Those slides give an excellent overview of how Python 2’s Unicode features were designed (where the Unicode string type goes by `unicode` and literals open with `u`).

### References

Within David Beazley’s PyCon 2010 talk [Mastering Python 3 Input/Output](https://pyvideo.org/video/289/pycon-2010--mastering-python-3-i-o), one segment covers handling text and working with binary data.

Character-encoding matters, plus how to internationalize and localize an application, are taken up in the [PDF slides for Marc-André Lemburg’s presentation “Writing Unicode-aware Applications in Python”](https://downloads.egenix.com/python/LSM2005-Developing-Unicode-aware-applications-in-Python.pdf). Note that those slides address Python 2.x exclusively.

In his PyCon 2013 talk [The Guts of Unicode in Python](https://pyvideo.org/video/1768/the-guts-of-unicode-in-python), Benjamin Peterson walks through how Python 3.3 represents Unicode internally.

[Subject index](INDEX.md) · [Previous source context](encodings.md) · [Following source context](python-s-unicode-support.md) · [Previous source context](unicode-regular-expressions.md) · [Following source context](reading-and-writing-unicode-data.md) · [Previous source context](files-in-an-unknown-encoding.md)
