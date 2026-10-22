# What’s New in Python 2.0 / New modules — atexit, codecs, filecmp, gettext, gzip, mmap, re, tabnanny, unicodedata, urllib, urllib.robotparser, webbrowser, winreg, zipfile

### New modules

Several fresh modules joined the library. What follows is just a quick enumeration with short notes; turn to the 2.0 documentation when you need the specifics of any one module.

- [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit): Lets you register functions that run just before the Python interpreter shuts down. Wherever code assigns `sys.exitfunc` on its own today, switch it over to the `atexit` module — import `atexit` and pass your exit-time function to [`atexit.register()`](https://docs.python.org/3.14/library/atexit.html#atexit.register). (Contributed by Skip Montanaro.)

- [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs), `encodings`, [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata): Brought in alongside the freshly introduced Unicode facilities.

- [`filecmp`](https://docs.python.org/3.14/library/filecmp.html#module-filecmp): Takes the place of the former `cmp`, `cmpcache` and `dircmp` modules, all of which are deprecated as of now. (Contributed by Gordon MacMillan and Moshe Zadka.)

- [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext): Gives Python programs internationalization (I18N) and localization (L10N) capabilities by wrapping the GNU gettext message catalog library. (Integrated by Barry Warsaw, drawing on independent contributions from Martin von Löwis, Peter Funk, and James Henstridge.)

- `linuxaudiodev`: Drives the `/dev/audio` device under Linux, mirroring the already-present `sunaudiodev` module. (Contributed by Peter Bosch, with fixes by Jeremy Hylton.)

- [`mmap`](https://docs.python.org/3.14/library/mmap.html#module-mmap): Offers access to memory-mapped files across both Windows and Unix. Once a file’s bytes are mapped straight into memory, the result acts like a mutable string whose contents you can both read and alter. You may even hand them to functions that look for plain strings, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module being one example. (Contributed by Sam Rushing, with some extensions by A.M. Kuchling.)

- `pyexpat`: Exposes the Expat XML parser through Python. (Contributed by Paul Prescod.)

- [`robotparser`](https://docs.python.org/3.14/library/urllib.robotparser.html#module-urllib.robotparser): Reads a `robots.txt` file, the mechanism by which web spiders are kept from courteously straying into off-limits parts of a site. Hand the parser the body of a `robots.txt` file and it assembles a rule set, after which it can tell you whether any particular URL is fetchable. (Contributed by Skip Montanaro.)

- [`tabnanny`](https://docs.python.org/3.14/library/tabnanny.html#module-tabnanny): Serves as both module and script for spotting indentation in Python source that could be read two ways. (Contributed by Tim Peters.)

- `UserString`: A handy base class from which to derive objects that act like strings.

- [`webbrowser`](https://docs.python.org/3.14/library/webbrowser.html#module-webbrowser): A module giving you a platform-neutral means of opening a web browser at a given URL. On every platform it works through a list of candidate browsers attempted in a fixed sequence. Which one ends up launching can be steered by the user through the *BROWSER* environment variable. (The idea traces back to Eric S. Raymond’s patch to [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib) that added comparable behaviour, yet the shipped module grew out of code Fred Drake first wrote as `Tools/idle/BrowserControl.py` and then reworked for the standard library.)

- [`_winreg`](https://docs.python.org/3.14/library/winreg.html#module-winreg): Provides a way to reach the Windows registry. `_winreg` reworks functions that had lived in PythonWin since 1995, now folded into the core distribution and extended with Unicode handling. `_winreg` is the work of Bill Tutt and Mark Hammond.

- [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile): A module that reads and writes archives in ZIP format. Such archives are what **PKZIP** turns out on DOS/Windows and what **zip** turns out on Unix — keep them distinct from **gzip**-format files, which the [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) module looks after. (Contributed by James C. Ahlstrom.)

- `imputil`: A module offering a more straightforward route to authoring custom import hooks than the `ihooks` module that already exists. (Implemented by Greg Stein, after plenty of back-and-forth on python-dev en route.)

[Subject index](INDEX.md) · [Previous source section](module-changes.md) · [Next source section](idle-improvements.md) · [Release/subject declaration](introduction.md)
