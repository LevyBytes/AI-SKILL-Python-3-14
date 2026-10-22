# warnings: `warnings.warn()`, `warnings.warn_explicit()`, `warnings.showwarning()`, `warnings.formatwarning()`, `warnings.filterwarnings()`, `warnings.simplefilter()`, `warnings.resetwarnings()`

### Available Functions

 warnings.warn(*message*, *category=None*, *stacklevel=1*, *source=None*, ***, *skip_file_prefixes=()*)

Raise a warning, or perhaps disregard it or raise an exception instead. The *category* argument, when provided, has to be a warning category class; absent that, it defaults to [`UserWarning`](https://docs.python.org/3.14/library/exceptions.html#UserWarning). As an alternative, *message* can itself be a [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning) instance, in which event *category* is disregarded and `message.__class__` takes its place. Under that arrangement, the message text becomes `str(message)`. Should the particular warning raised be converted into an error by the warnings filter, this function raises an exception. The *stacklevel* argument is there for wrapper functions written in Python to use, in this fashion:

```python
def deprecated_api(message):
    warnings.warn(message, DeprecationWarning, stacklevel=2)

```

That ties the warning to whoever called `deprecated_api`, instead of to where `deprecated_api` itself sits in the source (since the latter would undermine the very point of the warning message).

You can rely on the *skip_file_prefixes* keyword argument to say which stack frames should be passed over while counting stack levels. This comes in handy when you want the warning to keep showing up at call sites outside a package and a fixed *stacklevel* doesn't suit every call path or is otherwise awkward to keep accurate. When given, it has to be a tuple of strings. Once prefixes are given, stacklevel is silently forced to `max(2, stacklevel)`. To make a warning be attributed to whoever called in from outside the current package, you could write:

```python
# example/lower.py
_warn_skips = (os.path.dirname(__file__),)

def one_way(r_luxury_yacht=None, t_wobbler_mangrove=None):
    if r_luxury_yacht:
        warnings.warn("Please migrate to t_wobbler_mangrove=.",
                      skip_file_prefixes=_warn_skips)

# example/higher.py
from . import lower

def another_way(**kw):
    lower.one_way(**kw)

```

That makes the warning point at both the `example.lower.one_way()` and `example.higher.another_way()` call sites, but only when the calling code lives outside the `example` package.

*source*, when given, is the destroyed object that emitted a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning).

Changed in version 3.6: Added *source* parameter.

Changed in version 3.12: Added *skip_file_prefixes*.

 warnings.warn_explicit(*message*, *category*, *filename*, *lineno*, *module=None*, *registry=None*, *module_globals=None*, *source=None*)

This offers a low-level way into what `warn()` does, supplying the message, category, filename and line number explicitly, plus optional further arguments. Here *message* has to be a string while *category* must subclass [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning); alternatively *message* may itself be a `Warning` instance, whereupon *category* is disregarded.

*module*, when given, should hold the module name. Absent any module, the filename with `.py` stripped off serves instead.

*registry*, when given, should be the module's `__warningregistry__` dictionary. Absent any registry, every warning is treated as a first occurrence — that is, the filter actions `"default"`, `"module"` and `"once"` behave like `"always"`.

*module_globals*, when given, should be the global namespace that the code raising the warning is using. (This argument exists to support showing source for modules located in zipfiles or other non-filesystem import sources).

*source*, when given, is the destroyed object that emitted a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning).

Changed in version 3.6: Add the *source* parameter.

 warnings.showwarning(*message*, *category*, *filename*, *lineno*, *file=None*, *line=None*)

Write a warning out to a file. The default implementation invokes `formatwarning(message, category, filename, lineno, line)` and writes the resulting string to *file*, which defaults to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). By assigning to `warnings.showwarning` you may replace this function with any callable. The *line* parameter holds a source-code line to fold into the warning message; should *line* be omitted, `showwarning()` tries to read the line indicated by *filename* and *lineno*.

 warnings.formatwarning(*message*, *category*, *filename*, *lineno*, *line=None*)

Format a warning in the standard manner. The return value is a string that may carry embedded newlines and finishes with a newline. The *line* parameter holds a source-code line to fold into the warning message; should *line* be omitted, `formatwarning()` tries to read the line indicated by *filename* and *lineno*.

 warnings.filterwarnings(*action*, *message=''*, *category=Warning*, *module=''*, *lineno=0*, *append=False*)

Add an entry to the list of warnings filter specifications. The entry goes at the front by default; if *append* is true, it goes at the end instead. This validates the argument types, compiles the *message* and *module* regular expressions, and slots them as a tuple into the list of warnings filters. Where two entries both match a given warning, the one nearer the front of the list wins over the one further back. Any argument left out defaults to a value that matches everything.

 warnings.simplefilter(*action*, *category=Warning*, *lineno=0*, *append=False*)

Add a simple entry to the list of warnings filter specifications. The function parameters mean the same as for `filterwarnings()`, except that no regular expressions are required, since the inserted filter always matches any message in any module so long as the category and line number match.

 warnings.resetwarnings()

Reset the warnings filter. This undoes everything done by earlier calls to `filterwarnings()`, taking in the effect of the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) command line options and of calls to `simplefilter()`.

[Subject index](INDEX.md) · [Previous](updating-code-for-new-versions-of-dependencies.md) · [Continue](available-functions.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
