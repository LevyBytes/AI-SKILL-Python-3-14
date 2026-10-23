# optparse - How `optparse` handles errors

### How `optparse` handles errors

`optparse` has to concern itself with two broad categories of error: programmer errors and user errors. Programmer errors typically amount to mistaken calls to `OptionParser.add_option()`—for instance invalid option strings, unknown option attributes, or missing option attributes. These get the usual treatment: raise an exception (either `optparse.OptionError` or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError)) and let the program crash.

Coping with user errors matters far more, because they are certain to occur regardless of how solid your code is. `optparse` is able to catch certain user errors by itself: malformed option arguments (handing over `-n 4x` when `-n` wants an integer), or absent arguments (`-n` sitting at the very end of the command line while `-n` expects an argument of some type). On top of that, you may call `OptionParser.error()` to raise an application-defined error condition:

```python
(options, args) = parser.parse_args()
...
if options.a and options.b:
    parser.error("options -a and -b are mutually exclusive")

```

Whichever the case, `optparse` deals with the error identically: it writes the program's usage message plus an error message to standard error and exits with error status 2.

Take the first case above, in which the user hands `4x` to an option expecting an integer:

```shell
$ /usr/bin/foo -n 4x
Usage: foo [options]

foo: error: option -n: invalid integer value: '4x'

```

Or the case where the user supplies no value whatsoever:

```shell
$ /usr/bin/foo -n
Usage: foo [options]

foo: error: -n option requires an argument

```

Error messages produced by `optparse` always make a point of naming the option tied to the error; do likewise whenever your application code calls `OptionParser.error()`.

When `optparse`'s built-in error handling doesn't fit your requirements, you will have to subclass OptionParser and replace its `exit()` and/or `error()` methods.

[Subject index](INDEX.md) · [Previous](optionparser-print-version-to-optionparser-get-version.md) · [Continue](putting-it-all-together.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
