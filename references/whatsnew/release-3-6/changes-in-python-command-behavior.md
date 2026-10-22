# What's New In Python 3.6 / Changes in 'python' Command Behavior

### Changes in 'python' Command Behavior

- For a special Python build compiled with the `COUNT_ALLOCS`, `SHOW_ALLOC_COUNT` or `SHOW_TRACK_COUNT` macros defined, the output is now suppressed by default. Switch it back on with the `-X showalloccount` option. The data now goes to `stderr` rather than `stdout`. (Contributed by Serhiy Storchaka in [bpo-23034](https://bugs.python.org/issue?@action=redirect&bpo=23034).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-6.md) · [Next source section](changes-in-the-python-api.md) · [Release/subject declaration](summary-release-highlights.md)
