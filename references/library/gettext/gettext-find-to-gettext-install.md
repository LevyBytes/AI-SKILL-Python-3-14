# gettext - Class-based API

### Class-based API

Compared with the GNU **gettext** API, the class-based API of the `gettext` module offers you both added flexibility and more convenience. It is the suggested approach for localizing your Python applications and modules. `gettext` supplies a `GNUTranslations` class that handles parsing GNU `.mo` format files and exposes methods that return strings. Objects of this class can additionally register themselves within the built-in namespace under the function name `_()`.

 gettext.find(*domain*, *localedir=None*, *languages=None*, *all=False*)

This function carries out the standard `.mo` file search algorithm. It accepts a *domain*, the same as what `textdomain()` accepts. Optional *localedir* matches the meaning it has in `bindtextdomain()`. Optional *languages* is a list of strings, each one a language code.

When *localedir* is not supplied, the default system locale directory takes its place. [2] When *languages* is not supplied, these environment variables get inspected: `LANGUAGE`, `LC_ALL`, `LC_MESSAGES`, and `LANG`. The first to yield a non-empty value supplies the *languages* variable. Those environment variables ought to hold a colon separated list of languages, which gets split on the colon to form the expected list of language code strings.

`find()` next expands and normalizes the languages, then walks through them, hunting for an existing file assembled from these components:

`*localedir*/*language*/LC_MESSAGES/*domain*.mo`

`find()` returns the first such file name that exists. When no such file turns up, `None` is returned instead. When *all* is supplied, it yields a list of every file name, ordered as they occur in the languages list or the environment variables.

 gettext.translation(*domain*, *localedir=None*, *languages=None*, *class_=None*, *fallback=False*)

Yield a `*Translations` instance derived from the *domain*, *localedir*, and *languages*, which are first routed through `find()` to obtain a list of the related `.mo` file paths. Instances sharing the same `.mo` file names are cached. The class actually constructed is *class_* when supplied, and `GNUTranslations` otherwise. That class's constructor has to accept exactly one [file object](https://docs.python.org/3.14/glossary.html#term-file-object) argument.

When several files are located, the later ones serve as fallbacks for the earlier ones. So the fallback can be configured, [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) clones each translation object out of the cache; the underlying instance data nonetheless stays shared with the cache.

When no `.mo` file turns up, this function raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when *fallback* is false (the default), and yields a `NullTranslations` instance when *fallback* is true.

Changed in version 3.3: [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) was raised previously; it is now an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Changed in version 3.11: *codeset* parameter is removed.

 gettext.install(*domain*, *localedir=None*, ***, *names=None*)

This registers the function `_()` within Python's builtins namespace, derived from *domain* and *localedir*, both of which are forwarded to the function `translation()`.

Regarding the *names* parameter, consult the description of the translation object's `install()` method.

As shown below, you typically flag the strings in your application that qualify for translation by enclosing them in a call to the `_()` function, like this:

```python
print(_('This string will be translated.'))

```

As a convenience, having the `_()` function placed in Python's builtins namespace keeps it readily reachable from every module across your application.

Changed in version 3.11: *names* is now a keyword-only parameter.

[Subject index](INDEX.md) · [Previous](gettext-bindtextdomain-to-gettext-dnpgettext.md) · [Continue](gettext-nulltranslations-class.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
