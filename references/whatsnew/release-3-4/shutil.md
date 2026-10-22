# What's New In Python 3.4 / shutil — shutil

### shutil

[`copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile) now throws a dedicated [`Error`](https://docs.python.org/3.14/library/shutil.html#shutil.Error) subclass, [`SameFileError`](https://docs.python.org/3.14/library/shutil.html#shutil.SameFileError), whenever the source path and the destination path point at one identical file, letting a program react appropriately to that particular condition. (Contributed by Atsuo Ishimoto and Hynek Schlawack in [bpo-1492704](https://bugs.python.org/issue?@action=redirect&bpo=1492704).)

[Subject index](INDEX.md) · [Previous source section](shelve.md) · [Next source section](smtpd.md) · [Release/subject declaration](release-highlights.md)
