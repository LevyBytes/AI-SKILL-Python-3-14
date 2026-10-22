# What’s New in Python 2.3 / PEP 278: Universal Newline Support

### PEP 278: Universal Newline Support

Three operating systems dominate present-day computing: Microsoft Windows, Apple’s Macintosh OS, and the assorted Unix derivatives. One small annoyance in cross-platform development is that each of these three platforms marks the ends of lines in text files with a different character. The linefeed (ASCII character 10) is what Unix uses, MacOS relies on the carriage return (ASCII character 13), and Windows pairs a carriage return with a newline in a two-character sequence.

Beyond the line-ending convention native to whichever platform Python is executing on, Python’s file objects can now cope with the others as well. Open a file using the mode `'U'` or `'rU'` and it opens for reading in [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) mode. Each of the three line ending conventions then comes back as `'\n'` within the strings handed back by the assorted file methods, `read()` and `readline()` among them.

That same universal newline handling kicks in when modules are imported and when a file is run via the `execfile()` function. As a result, the same Python modules can be passed among all three operating systems with no need to fix up their line-endings.

If you would rather not have this feature, you can switch it off at compile time by handing the `--without-universal-newlines` switch to Python’s **configure** script.

See also

[**PEP 278**](https://peps.python.org/pep-0278/) - Universal Newline Support

Written and implemented by Jack Jansen.

[Subject index](INDEX.md) · [Previous source section](pep-277-unicode-file-name-support-for-windows-nt.md) · [Next source section](pep-279-enumerate.md) · [Release/subject declaration](standard-set-type.md)
