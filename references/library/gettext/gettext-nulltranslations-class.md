# gettext: `gettext.NullTranslations`

### The `NullTranslations` class

The actual conversion of original source file message strings into translated message strings is carried out by translation classes. Every translation class derives from the base class `NullTranslations`; it supplies the foundational interface you can build on to author your own specialized translation classes. The methods of `NullTranslations` are listed here:

 *class *gettext.NullTranslations(*fp=None*)

Accepts an optional [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *fp*, which the base class disregards. It initializes the "protected" instance variables *_info* and *_charset*, which derived classes assign, along with *_fallback*, assigned via `add_fallback()`. It then invokes `self._parse(fp)` whenever *fp* is not `None`.

[Subject index](INDEX.md) · [Previous](gettext-find-to-gettext-install.md) · [Continue](null-translations-parsing-and-installation.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
