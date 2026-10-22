# 5.2. Packages

### 5.2. Packages

There is just a single kind of module object in Python, and every module shares that kind, no matter whether it was written in Python, in C, or in anything else. So that modules can be grouped sensibly and given a hierarchy of names, Python offers the notion of [packages](https://docs.python.org/3.14/glossary.html#term-package).

It helps to picture packages as directories on a file system and modules as the files sitting inside those directories, yet you shouldn’t lean on that comparison too hard, because neither packages nor modules have to come from a file system at all. Throughout this documentation, though, we’ll lean on that handy directories-and-files comparison. Just as file system directories nest, packages are arranged hierarchically, and a package may hold subpackages of its own alongside ordinary modules.

Bear in mind that every package qualifies as a module, while the reverse does not hold for every module. Said differently, a package is merely one particular flavor of module. To be exact, a module counts as a package precisely when it carries a `__path__` attribute.

A name belongs to every module. A subpackage’s name is set off from the name of its enclosing package by a dot, mirroring Python’s ordinary syntax for reaching attributes. So you could have a package named [`email`](https://docs.python.org/3.14/library/email.html#module-email) that holds a subpackage named [`email.mime`](https://docs.python.org/3.14/library/email.mime.html#module-email.mime), inside which sits a module named [`email.mime.text`](https://docs.python.org/3.14/library/email.mime.html#module-email.mime.text).

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](importlib.md) · [Following source section](regular-packages.md)
