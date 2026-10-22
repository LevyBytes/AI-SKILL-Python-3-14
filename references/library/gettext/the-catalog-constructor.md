# gettext — The Catalog constructor

### The Catalog constructor

GNOME relies on a variant of the `gettext` module written by James Henstridge, though that variant carries a somewhat different API. Its documented usage went as follows:

```python
import gettext
cat = gettext.Catalog(domain, localedir)
_ = cat.gettext
print(_('hello world'))

```

To stay compatible with that older module, the function `Catalog()` exists as an alias for the `translation()` function described earlier.

A single difference separates this module from Henstridge's: his catalog objects allowed access through a mapping API, but since that seems to go unused it is not currently supported.

[Subject index](INDEX.md) · [Previous](solaris-message-catalog-support.md) · [Continue](internationalizing-your-programs-and-modules.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
