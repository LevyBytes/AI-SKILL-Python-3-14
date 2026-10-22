# gettext: `gettext.GNUTranslations`

### The `GNUTranslations` class

The `gettext` module supplies one further class derived from `NullTranslations`: `GNUTranslations`. This class overrides `_parse()` so it can read GNU **gettext** format `.mo` files in both big-endian and little-endian layouts.

`GNUTranslations` pulls optional metadata out of the translation catalog. By GNU **gettext** convention the metadata is carried as the translation for the empty string. This metadata takes the form of [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html)-style `key: value` pairs and ought to include the `Project-Id-Version` key. When the key `Content-Type` is present, the `charset` property serves to initialize the "protected" `_charset` instance variable, which falls back to `None` when absent. When the charset encoding is given, every message id and message string read from the catalog gets converted to Unicode using that encoding; otherwise ASCII is assumed.

Because message ids are likewise read as Unicode strings, all `*gettext()` methods will treat message ids as Unicode strings rather than byte strings.

The complete collection of key/value pairs is loaded into a dictionary and stored as the "protected" `_info` instance variable.

Should the `.mo` file carry an invalid magic number, an unexpected major version number, or should some other trouble crop up during the file read, constructing a `GNUTranslations` class may raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 *class *gettext.GNUTranslations

These methods override the base class implementation:

[Subject index](INDEX.md) · [Previous](null-translations-parsing-and-installation.md) · [Continue](gnu-translations-singular-plural-and-context.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
