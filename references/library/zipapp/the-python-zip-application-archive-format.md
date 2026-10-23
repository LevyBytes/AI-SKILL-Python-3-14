# zipapp - The Python Zip Application Archive Format

### The Python Zip Application Archive Format

Since release 2.6, Python has been capable of running zip files that hold a `__main__.py` file. For Python to run it, an application archive need only be an ordinary zip file containing a `__main__.py` file, which serves as the application’s entry point. As with any Python script, the script’s parent — here the zip file — is set on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), so additional modules can be imported out of the zip file.

The zip file format permits arbitrary data to be placed ahead of a zip file. The zip application format taps that to put a standard POSIX “shebang” line at the front of the file (`#!/path/to/interpreter`).

Stated formally, then, the Python zip application format is:

1.

An optional shebang line made of the characters `b'#!'`, then an interpreter name, then a newline (`b'\n'`) character. The interpreter name may be whatever the OS “shebang” processing, or the Windows Python launcher, will accept. Encode the interpreter in UTF-8 on Windows and in [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) on POSIX.

2.

Ordinary zipfile data of the kind the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) module produces. That zipfile content *must* carry a file named `__main__.py` (which has to sit at the zipfile’s “root” — i.e., never in a subdirectory). The zipfile data may be compressed or not.

Where an application archive carries a shebang line, it can have the executable bit set on POSIX systems so it runs directly.

Nothing obliges you to build application archives with this module’s tools — the module is merely a convenience, and archives in the format above made by any means whatsoever are fine by Python.

[Subject index](INDEX.md) · [Previous](caveats.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)
