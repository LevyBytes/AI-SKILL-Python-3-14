# gettext — Localizing your application

### Localizing your application

When you are localizing your application, you can register the `_()` function globally into the built-in namespace, typically within the main driver file of your application. That lets all your application-specific files simply use `_('...')` without having to install it explicitly in each file.

For the simple case, then, you need only add this snippet of code to the main driver file of your application:

```python
import gettext
gettext.install('myapplication')

```

Should you need to set the locale directory, you can supply it to the `install()` function:

```python
import gettext
gettext.install('myapplication', '/usr/share/locale')

```

[Subject index](INDEX.md) · [Previous](localizing-your-module.md) · [Continue](changing-languages-on-the-fly.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
