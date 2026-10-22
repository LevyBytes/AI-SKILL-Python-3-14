# gettext — GNU **gettext** API

### GNU **gettext** API

Below is the API exposed by the `gettext` module, closely mirroring the GNU **gettext** API. Relying on this API influences translation across your whole application at a global scope. That behavior is frequently desirable for a monolingual application, where the language picked follows the locale of your user. For localizing a single Python module, or when your application must change languages dynamically, the class-based API is the better fit.

 gettext.bindtextdomain(*domain*, *localedir=None*)

Associate the *domain* with the locale directory *localedir*. Put differently, `gettext` searches for binary `.mo` files belonging to the named domain along this path (on Unix): `*localedir*/*language*/LC_MESSAGES/*domain*.mo`, where *language* is looked up across the environment variables `LANGUAGE`, `LC_ALL`, `LC_MESSAGES`, and `LANG` in that order.

When *localedir* is left out or set to `None`, the existing binding for *domain* is given back. [1]

 gettext.textdomain(*domain=None*)

Set or read the current global domain. When *domain* is `None`, the present global domain is returned; otherwise the global domain becomes *domain*, and that value is returned.

 gettext.gettext(*message*, */*)

Hand back the localized translation of *message*, keyed off the current global domain, language, and locale directory. Conventionally this function gets aliased to `_()` within the local namespace (refer to the examples that follow).

 gettext.dgettext(*domain*, *message*, */*)

Behaves like `gettext()`, except the message is resolved in the named *domain*.

 gettext.ngettext(*singular*, *plural*, *n*, */*)

Behaves like `gettext()`, but accounts for plural forms. When a translation exists, the plural formula is applied to *n* and the resulting message is returned (certain languages carry more than two plural forms). When no translation exists, *singular* is returned if *n* is 1; otherwise *plural* is returned.

The Plural formula comes from the catalog header. It is a C or Python expression carrying a single free variable *n*; evaluating the expression yields the index of the plural within the catalog. Consult [the GNU gettext documentation](https://www.gnu.org/software/gettext/manual/gettext.html) for the exact syntax expected in `.po` files together with the formulas covering many languages.

 gettext.dngettext(*domain*, *singular*, *plural*, *n*, */*)

Behaves like `ngettext()`, except the message is resolved in the named *domain*.

 gettext.pgettext(*context*, *message*, */*)

 gettext.dpgettext(*domain*, *context*, *message*, */*)

 gettext.npgettext(*context*, *singular*, *plural*, *n*, */*)

 gettext.dnpgettext(*domain*, *context*, *singular*, *plural*, *n*, */*)

These parallel the matching functions lacking the `p` prefix (namely `gettext()`, `dgettext()`, `ngettext()`, `dngettext()`), except translation is confined to the supplied message *context*.

Added in version 3.8.

Keep in mind that GNU **gettext** additionally specifies a `dcgettext()` method, yet it was judged not useful and therefore remains unimplemented for now.

A representative example of how this API is normally used:

```python
import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
# ...
print(_('This is a translatable string.'))

```

[Subject index](INDEX.md) · [Previous](gettext-multilingual-internationalization-services.md) · [Continue](gettext-find-to-gettext-install.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
