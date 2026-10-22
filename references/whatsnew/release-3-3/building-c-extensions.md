# What's New In Python 3.3 / Building C extensions

### Building C extensions

- Which file names can stand in for C extensions has been tightened. A few seldom-used spellings are now disallowed: on POSIX, the files `xxxmodule.so`, `xxxmodule.abi3.so` and `xxxmodule.cpython-*.so` are no longer treated as providing the `xxx` module. Anyone producing such files must move to the alternative spellings — that is, strip the `module` string out of the file names.

(implemented in [bpo-14040](https://bugs.python.org/issue?@action=redirect&bpo=14040).)

[Subject index](INDEX.md) · [Previous source section](porting-c-code.md) · [Next source section](command-line-switch-changes.md) · [Release/subject declaration](summary-release-highlights.md)
