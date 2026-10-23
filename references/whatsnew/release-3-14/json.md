# What's new in Python 3.14 / json - json

### json

- JSON serialization failures now attach exception notes that pinpoint where the trouble began. (Contributed by Serhiy Storchaka in [gh-122163](https://github.com/python/cpython/issues/122163).)

- The [`json`](https://docs.python.org/3.14/library/json.html#module-json) module can now run as a script through the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch: **python -m json**. That form is favored over **python -m json.tool**, which has become [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Refer to the [JSON command-line interface](https://docs.python.org/3.14/library/json.html#json-commandline) documentation. (Contributed by Trey Hunner in [gh-122873](https://github.com/python/cpython/issues/122873).)

- By default the [JSON command-line interface](https://docs.python.org/3.14/library/json.html#json-commandline) emits colorized output. This behavior responds to [environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color). (Contributed by Tomas Roun in [gh-131952](https://github.com/python/cpython/issues/131952).)

[Subject index](INDEX.md) · [Previous source section](io.md) · [Next source section](linecache.md) · [Release/subject declaration](summary-release-highlights.md)
