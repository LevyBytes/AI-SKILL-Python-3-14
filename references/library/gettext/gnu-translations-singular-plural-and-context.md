# gettext.GNUTranslations: `gettext()`, `ngettext()`, `pgettext()`, `npgettext()`

gettext(*message*, */*)

Resolve the *message* id within the catalog and give back the matching message string, as a Unicode string. When the catalog holds no entry for the *message* id and a fallback has been registered, the lookup is routed to the fallback's `gettext()` method. Otherwise, the *message* id itself is returned.

 ngettext(*singular*, *plural*, *n*, */*)

Perform a plural-forms lookup for a message id. *singular* serves as the message id for the catalog lookup, while *n* decides which plural form applies. The message string returned is a Unicode string.

When the message id is absent from the catalog and a fallback is given, the request is routed to the fallback's `ngettext()` method. Otherwise, *singular* is returned when *n* is 1, and *plural* is returned in every other case.

Here is an example:

```python
n = len(os.listdir('.'))
cat = GNUTranslations(somefile)
message = cat.ngettext(
    'There is %(num)d file in this directory',
    'There are %(num)d files in this directory',
    n) % {'num': n}

```

 pgettext(*context*, *message*, */*)

Resolve the *context* and *message* id within the catalog and give back the matching message string, as a Unicode string. When the catalog holds no entry for the *message* id and *context*, and a fallback has been registered, the lookup is routed to the fallback's `pgettext()` method. Otherwise, the *message* id itself is returned.

Added in version 3.8.

 npgettext(*context*, *singular*, *plural*, *n*, */*)

Perform a plural-forms lookup for a message id. *singular* serves as the message id for the catalog lookup, while *n* decides which plural form applies.

When the message id for *context* is absent from the catalog and a fallback is given, the request is routed to the fallback's `npgettext()` method. Otherwise, *singular* is returned when *n* is 1, and *plural* is returned in every other case.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](gettext-gnutranslations-class.md) · [Continue](solaris-message-catalog-support.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md) · [Owning module, declaration or section: gettext.GNUTranslations](gettext-gnutranslations-class.md) · [Owning module, declaration or section: The `GNUTranslations` class](gettext-gnutranslations-class.md)
