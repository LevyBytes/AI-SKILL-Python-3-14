# Python 3.2 changes: Restored callable builtin and core language changes

The Py2.x [`callable()`](https://docs.python.org/3.14/library/functions.html#callable) builtin function has been brought back. It gives a short, legible substitute for reaching for an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) inside an expression such as `isinstance(x, collections.Callable)`:

```python
>>> callable(max)
True
>>> callable(20)
False

```

(See [bpo-10518](https://bugs.python.org/issue?@action=redirect&bpo=10518).)

- Python's import machinery is now able to load modules placed in directories whose path names carry non-ASCII characters. That fixed an irritating issue affecting home directories belonging to users whose usernames include non-ASCII characters.

>

(Required extensive work by Victor Stinner in [bpo-9425](https://bugs.python.org/issue?@action=redirect&bpo=9425).)

[Subject index](INDEX.md) · [Previous source section](other-language-changes-f.md) · [Next source section](new-improved-and-deprecated-modules.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Release/subject declaration](core-language-changes.md) · [Preceding release/subject continuation](other-language-changes-outer.md)
