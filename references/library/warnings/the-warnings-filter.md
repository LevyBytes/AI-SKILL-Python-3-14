# warnings — The Warnings Filter

### The Warnings Filter

Whether a warning is ignored, shown, or escalated into an error (raising an exception) is governed by the warnings filter.

Think of the warnings filter as keeping an ordered list of filter specifications; a given warning is checked against each specification in that list one after another until something matches, and the matching filter decides what happens to that warning. Every entry is a tuple shaped like (*action*, *message*, *category*, *module*, *lineno*), in which:

- *action* is one of the following strings:

| Value | Disposition |
| --- | --- |
| `"default"` | show only the initial matching warning per location (module + line number) at which it arises |
| `"error"` | escalate matching warnings to exceptions |
| `"ignore"` | suppress matching warnings entirely |
| `"always"` | display matching warnings every time |
| `"all"` | alias to “always” |
| `"module"` | show only the initial matching warning per module where it arises (line number aside) |
| `"once"` | show just the initial matching warning, no matter the location |

- *message* holds a regular expression, and the beginning of the warning message has to match it case-insensitively. Within [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) and [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS), *message* is instead a plain string that the start of the warning message must contain (case-insensitively), with any leading or trailing whitespace in *message* dropped.

- *category* names a class (a subclass of [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning)); for a match, the warning's category has to be a subclass of it.

- *module* holds a regular expression, and the beginning of the fully qualified module name has to match it case-sensitively. Within [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) and [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS), *module* is instead a plain string that the fully qualified module name has to equal exactly (case-sensitively), with any leading or trailing whitespace in *module* dropped.

- *lineno* is an integer; either the line number at which the warning arose has to equal it, or it is `0` to match every line number.

Because the [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning) class descends from the built-in [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) class, promoting a warning to an error is as simple as raising `category(message)`.

Whenever a reported warning matches none of the registered filters, the “default” action takes over (which is where its name comes from).

[Subject index](INDEX.md) · [Previous](warning-categories.md) · [Continue](repeated-warning-suppression-criteria.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
