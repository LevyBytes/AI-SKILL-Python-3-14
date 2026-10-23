# What's New In Python 3.3 / PEP 421: Adding sys.implementation - importlib, sys

### PEP 421: Adding sys.implementation

A fresh attribute on the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module surfaces particulars tied to the implementation of whichever interpreter is currently running. The first batch of attributes that [`sys.implementation`](https://docs.python.org/3.14/library/sys.html#sys.implementation) carries are `name`, `version`, `hexversion`, and `cache_tag`.

The aim behind `sys.implementation` is to gather into one namespace the implementation-specific data the standard library relies on. That makes it far easier for distinct Python implementations to share one common standard library code base. To begin with, `sys.implementation` keeps only a modest slice of the implementation-specific data. As time passes, that proportion will grow so the standard library becomes more portable.

The `cache_tag` is one example of better standard library portability. Starting in Python 3.3, [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) leans on `sys.implementation.cache_tag` to back [**PEP 3147**](https://peps.python.org/pep-3147/) compliance. Whatever Python implementation drives its built-in import system through `importlib` may turn to `cache_tag` to govern how modules are cached.

### SimpleNamespace end

[Subject index](INDEX.md) · [Previous source section](pep-362-function-signature-object.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](simplenamespace-end.md)
