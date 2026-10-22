# What's New In Python 3.6 / PEP 529: Change Windows filesystem encoding to UTF-8 — os, sys

### PEP 529: Change Windows filesystem encoding to UTF-8

The strongest way to model filesystem paths is with str (Unicode) instead of bytes. That said, a handful of cases exist where bytes will do the job correctly.

Before Python 3.6, feeding bytes paths to Windows risked losing data. After this change, Windows accepts bytes as a way to model paths, so long as those bytes carry the encoding handed back by [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding), which now falls back to `'utf-8'`.

Any application that avoids str for paths ought to reach for [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) and [`os.fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode) so its bytes carry the right encoding. To go back to the earlier behaviour, set [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) or invoke [`sys._enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding).

Refer to [**PEP 529**](https://peps.python.org/pep-0529/) for the full story and a discussion of any code edits that might be needed.

[Subject index](INDEX.md) · [Previous source section](pep-495-local-time-disambiguation.md) · [Next source section](pep-528-change-windows-console-encoding-to-utf-8.md) · [Release/subject declaration](summary-release-highlights.md)
