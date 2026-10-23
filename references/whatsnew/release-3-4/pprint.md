# What's New In Python 3.4 / pprint - pprint

### pprint

The [`pprint`](https://docs.python.org/3.14/library/pprint.html#module-pprint) module's [`PrettyPrinter`](https://docs.python.org/3.14/library/pprint.html#pprint.PrettyPrinter) class along with its [`pformat()`](https://docs.python.org/3.14/library/pprint.html#pprint.pformat), and [`pprint()`](https://docs.python.org/3.14/library/pprint.html#pprint.pprint) functions gained a fresh option, *compact*, governing the layout of the output. For now, turning *compact* to `True` makes sequences print as many sequence elements as fit inside *width* on each (indented) line. (Contributed by Serhiy Storchaka in [bpo-19132](https://bugs.python.org/issue?@action=redirect&bpo=19132).)

Lengthy strings are wrapped these days using Python's standard line continuation syntax. (Contributed by Antoine Pitrou in [bpo-17150](https://bugs.python.org/issue?@action=redirect&bpo=17150).)

[Subject index](INDEX.md) · [Previous source section](poplib.md) · [Next source section](pty.md) · [Release/subject declaration](release-highlights.md)
