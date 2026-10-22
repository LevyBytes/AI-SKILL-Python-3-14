# What's New In Python 3.4 / Changes in 'python' Command Behavior — argparse

### Changes in 'python' Command Behavior

- Inside a posix shell, giving the `PATH` environment variable an empty value amounts to leaving it unset. By contrast, giving [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) an empty value did *not* amount to leaving it unset: an empty `PYTHONPATH` behaved as though it held `.`, a source of confusion for anyone reasoning from how `PATH` behaves. That handling now lines up with the posix rule for `PATH`.

- In a debug (`--with-pydebug`) build, the CPython interpreter's [X refs, Y blocks] line is now suppressed by default. Switch it back on with the `-X showrefcount` option. (Contributed by Ezio Melotti in [bpo-17323](https://bugs.python.org/issue?@action=redirect&bpo=17323).)

- The python command together with most stdlib scripts (and likewise [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse)) now print `--version` details to `stdout` rather than `stderr` (refer to Other Improvements above for the list of issues).

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-4.md) · [Next source section](changes-in-the-python-api.md) · [Release/subject declaration](release-highlights.md)
