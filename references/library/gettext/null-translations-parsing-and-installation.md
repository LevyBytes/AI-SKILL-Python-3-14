# gettext.NullTranslations: `_parse()`, `add_fallback()`, `gettext()`, `ngettext()`, `pgettext()`, `npgettext()`, `info()`, `charset()`, `install()`

_parse(*fp*)

A no-op in the base class, this method accepts file object *fp*, reads the data out of the file, and initializes its message catalog. When your message catalog file format is unsupported, you ought to override this method so it parses your format.

 add_fallback(*fallback*)

Register *fallback* as the fallback object for the present translation object. A translation object ought to defer to the fallback whenever it cannot supply a translation for a particular message.

 gettext(*message*, */*)

When a fallback has been registered, route `gettext()` to the fallback. Otherwise, give back *message*. Overridden within derived classes.

 ngettext(*singular*, *plural*, *n*, */*)

When a fallback has been registered, route `ngettext()` to the fallback. Otherwise, give back *singular* if *n* is 1; give back *plural* otherwise. Overridden within derived classes.

 pgettext(*context*, *message*, */*)

When a fallback has been registered, route `pgettext()` to the fallback. Otherwise, give back the translated message. Overridden within derived classes.

Added in version 3.8.

 npgettext(*context*, *singular*, *plural*, *n*, */*)

When a fallback has been registered, route `npgettext()` to the fallback. Otherwise, give back the translated message. Overridden within derived classes.

Added in version 3.8.

 info()

Give back a dictionary holding the metadata located in the message catalog file.

 charset()

Give back the encoding of the message catalog file.

 install(*names=None*)

This method registers `gettext()` into the built-in namespace, binding it to `_`.

When the *names* parameter is supplied, it has to be a sequence holding the names of functions you want registered in the builtins namespace alongside `_()`. The supported names are `'gettext'`, `'ngettext'`, `'pgettext'`, and `'npgettext'`.

Bear in mind this is merely one approach — though the handiest — to expose the `_()` function to your application. Because it touches the whole application globally, and in particular the built-in namespace, localized modules should never install `_()`. They should instead use this code to make `_()` reachable within their module:

```python
import gettext
t = gettext.translation('mymodule', ...)
_ = t.gettext

```

That places `_()` solely in the module's global namespace, so it affects only calls made inside this module.

Changed in version 3.8: Added `'pgettext'` and `'npgettext'`.

[Subject index](INDEX.md) · [Previous](gettext-nulltranslations-class.md) · [Continue](gettext-gnutranslations-class.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md) · [Owning module, declaration or section: gettext.NullTranslations](gettext-nulltranslations-class.md) · [Owning module, declaration or section: The `NullTranslations` class](gettext-nulltranslations-class.md)
