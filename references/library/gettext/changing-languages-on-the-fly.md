# gettext - Changing languages on the fly

### Changing languages on the fly

When your program must support many languages simultaneously, you may wish to build several translation instances and then toggle between them explicitly, like so:

```python
import gettext

lang1 = gettext.translation('myapplication', languages=['en'])
lang2 = gettext.translation('myapplication', languages=['fr'])
lang3 = gettext.translation('myapplication', languages=['de'])

# start by using language1
lang1.install()

# ... time goes by, user selects language 2
lang2.install()

# ... more time goes by, user selects language 3
lang3.install()

```

[Subject index](INDEX.md) · [Previous](localizing-your-application.md) · [Continue](deferred-translations.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
