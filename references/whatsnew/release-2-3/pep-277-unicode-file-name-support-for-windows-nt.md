# What’s New in Python 2.3 / PEP 277: Unicode file name support for Windows NT - os, os.path

### PEP 277: Unicode file name support for Windows NT

Across Windows NT, 2000, and XP, file names are kept by the system as Unicode strings. Python has historically held file names as byte strings, an approach that falls short because it leaves certain file names out of reach.

Every function that takes a file name — the [`open()`](https://docs.python.org/3.14/library/functions.html#open) built-in function being the most prominent — now accepts any Unicode string Python passes it (within whatever the file system permits). Hand a Unicode string to [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir) and Python hands back a list of Unicode strings. There is a new function as well, `os.getcwdu()`, that gives the current directory back as a Unicode string.

Byte strings continue to function as file names, and under Windows Python silently turns them into Unicode by means of the `mbcs` encoding.

Unicode strings are accepted as file names on other systems too, but there they get turned into byte strings ahead of being handed to the system, a step that may trigger a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError). To learn whether arbitrary Unicode strings will work as file names, an application can inspect [`os.path.supports_unicode_filenames`](https://docs.python.org/3.14/library/os.path.html#os.path.supports_unicode_filenames), which holds a Boolean value.

On MacOS, [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir) is now able to give back Unicode filenames.

See also

[**PEP 277**](https://peps.python.org/pep-0277/) - Unicode file name support for Windows NT

Authored by Neil Hodgson; the implementation was the work of Neil Hodgson, along with Martin von Löwis and Mark Hammond.

[Subject index](INDEX.md) · [Previous source section](pep-273-importing-modules-from-zip-archives.md) · [Next source section](pep-278-universal-newline-support.md) · [Release/subject declaration](standard-set-type.md)
