# gettext - Localizing your module

### Localizing your module

When you are localizing your module, you must be careful to avoid global changes, for example to the built-in namespace. Rather than the GNU **gettext** API, you should use the class-based API.

Suppose your module bears the name "spam" and the module's assorted natural language translation `.mo` files live in `/usr/share/locale` in GNU **gettext** format. Here is what you would place at the top of your module:

```python
import gettext
t = gettext.translation('spam', '/usr/share/locale')
_ = t.gettext

```

[Subject index](INDEX.md) · [Previous](internationalizing-your-programs-and-modules.md) · [Continue](localizing-your-application.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
