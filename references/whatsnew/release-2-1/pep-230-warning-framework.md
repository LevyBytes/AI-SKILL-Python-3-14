# What’s New in Python 2.1 / PEP 230: Warning Framework - __main__, re, warnings

### PEP 230: Warning Framework

Across the 10 years it’s been around, Python has picked up a number of stale modules and features along the road. Judging when a feature can be safely dropped is hard, because there’s no way to gauge how heavily it’s used — maybe nothing at all depends on it, or maybe plenty of programs do. So that old features could be retired in a more orderly fashion, a warning framework was introduced. When the Python developers decide to retire a feature, the next version of Python first emits a warning about it. The version after that can then remove the feature, leaving users a complete release cycle to strip out their reliance on the old one.

Python 2.1 supplies the warning framework that drives this approach. It introduces a [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module offering functions both to raise warnings and to screen out ones you’d rather not see. Third-party modules can lean on this framework as well to mark as deprecated old features they’d prefer to stop supporting.

To illustrate, under Python 2.1 the `regex` module carries a deprecation, so importing it prints a warning:

```python
>>> import regex
__main__:1: DeprecationWarning: the regex module
         is deprecated; please use the re module
>>>

```

You raise warnings by invoking the [`warnings.warn()`](https://docs.python.org/3.14/library/warnings.html#warnings.warn) function:

```python
warnings.warn("feature X no longer supported")

```

That first parameter holds the warning message; one further optional parameter lets you indicate a specific warning category.

You can attach filters to switch off particular warnings; a regular expression pattern may be matched against the message or the module name so a warning gets suppressed. Suppose, for instance, you run a program relying on the `regex` module and you’d rather not invest the time to migrate it to the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module just yet. The warning is silenced by calling

```python
import warnings
warnings.filterwarnings(action = 'ignore',
                        message='.*regex module is deprecated',
                        category=DeprecationWarning,
                        module = '__main__')

```

This registers a filter targeting only warnings of class [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) raised in the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module, applies a regular expression that matches solely the message about the `regex` module’s deprecation, and so makes those warnings get ignored. Warnings may instead be shown a single time, shown on every run of the offending code, or escalated into exceptions that halt the program (unless, of course, you catch those exceptions in the customary manner).

Python’s C API likewise gained functions for raising warnings; see PEP 230 or Python’s API documentation for the specifics.

See also

[**PEP 5**](https://peps.python.org/pep-0005/) - Guidelines for Language Evolution

Authored by Paul Prescod to lay out the steps that should govern retiring old features from Python. While this PEP’s described policy was never formally adopted, whatever policy ultimately emerges likely won’t stray far from what Prescod proposed.

[**PEP 230**](https://peps.python.org/pep-0230/) - Warning Framework

Written and implemented by Guido van Rossum.

[Subject index](INDEX.md) · [Previous source section](pep-207-rich-comparisons.md) · [Next source section](pep-229-new-build-system.md) · [Release/subject declaration](introduction.md)
