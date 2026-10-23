# What’s New In Python 3.5 / locale - locale

### locale

Honoring the `LC_NUMERIC` settings, a new [`delocalize()`](https://docs.python.org/3.14/library/locale.html#locale.delocalize) function turns a string into a normalized number string:

```python
>>> import locale
>>> locale.setlocale(locale.LC_NUMERIC, 'de_DE.UTF-8')
'de_DE.UTF-8'
>>> locale.delocalize('1.234,56')
'1234.56'
>>> locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')
'en_US.UTF-8'
>>> locale.delocalize('1,234.56')
'1234.56'

```

(Contributed by Cédric Krier in [bpo-13918](https://bugs.python.org/issue?@action=redirect&bpo=13918).)

[Subject index](INDEX.md) · [Previous source section](linecache.md) · [Next source section](logging.md) · [Release/subject declaration](summary-release-highlights.md)
