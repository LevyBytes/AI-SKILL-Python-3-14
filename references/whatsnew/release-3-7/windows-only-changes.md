# What's New In Python 3.7 / Windows-only Changes

### Windows-only Changes

The python launcher, (py.exe), is now able to take 32 & 64 bit specifiers **without** also requiring a minor version to be given. Hence `py -3-32` and `py -3-64` are valid, as is `py -3.7-32`; furthermore the -*m*-64 and -*m.n*-64 forms are now accepted to compel 64 bit python where 32 bit would otherwise have been chosen. py.exe exits with an error if the requested version is unavailable. (Contributed by Steve Barnes in [bpo-30291](https://bugs.python.org/issue?@action=redirect&bpo=30291).)

Invoking the launcher as `py -0` yields a listing of the installed pythons, *with default marked with an asterisk*. Adding `py -0p` will also show the paths. Should py run with a version specifier that has no match, it additionally prints the *short form* list of available specifiers. (Contributed by Steve Barnes in [bpo-30362](https://bugs.python.org/issue?@action=redirect&bpo=30362).)

[Subject index](INDEX.md) · [Previous source section](module-removals.md) · [Next source section](porting-to-python-3-7.md) · [Release/subject declaration](summary-release-highlights.md)
