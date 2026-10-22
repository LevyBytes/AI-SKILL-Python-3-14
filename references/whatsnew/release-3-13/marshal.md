# What's New In Python 3.13 / marshal

### marshal

- A new *allow_code* parameter joins the module's functions. Supplying `allow_code=False` blocks serialization and de-serialization of code objects, which differ across Python releases. (Contributed by Serhiy Storchaka in [gh-113626](https://github.com/python/cpython/issues/113626).)

[Subject index](INDEX.md) · [Previous source section](itertools.md) · [Next source section](math.md) · [Release/subject declaration](summary-release-highlights.md)
