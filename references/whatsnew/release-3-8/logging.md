# What’s New In Python 3.8 / logging - logging

> (Contributed by Weipeng Hong in [bpo-31553](https://bugs.python.org/issue?@action=redirect&bpo=31553).)

### logging

A *force* keyword argument has been added to [`logging.basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig). Setting it true tears down and closes whatever handlers are already on the root logger before the configuration named by the remaining arguments gets applied.

This clears up a problem that lingered for ages. After a logger or *basicConfig()* had run once, any later *basicConfig()* calls would just be dropped without notice. That made tweaking, exploring, or teaching the assorted logging configuration choices awkward from the interactive prompt or inside a Jupyter notebook.

[Subject index](INDEX.md) · [Previous source section](json-tool.md) · [Next source section](math.md) · [Release/subject declaration](assignment-expressions.md)
