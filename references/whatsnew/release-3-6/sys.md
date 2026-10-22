# What's New In Python 3.6 / sys — sys

### sys

The error mode that governs conversion between Unicode filenames and bytes filenames now has its name returned by the fresh [`getfilesystemencodeerrors()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencodeerrors) function. (Contributed by Steve Dower in [bpo-27781](https://bugs.python.org/issue?@action=redirect&bpo=27781).)

Under Windows, what [`getwindowsversion()`](https://docs.python.org/3.14/library/sys.html#sys.getwindowsversion) returns now carries a *platform_version* field holding the true major version, minor version and build number of the running operating system, instead of whatever version the process is being emulated as (Contributed by Steve Dower in [bpo-27932](https://bugs.python.org/issue?@action=redirect&bpo=27932).)

[Subject index](INDEX.md) · [Previous source section](subprocess.md) · [Next source section](telnetlib.md) · [Release/subject declaration](summary-release-highlights.md)
