# What's new in Python 3.14 / sys — sys

### sys

- The formerly undocumented special function [`sys.getobjects()`](https://docs.python.org/3.14/library/sys.html#sys.getobjects), present only in specialized builds of Python, can now hand back objects belonging to interpreters other than the one from which it’s invoked. (Contributed by Eric Snow in [gh-125286](https://github.com/python/cpython/issues/125286).)

- Add [`sys._is_immortal()`](https://docs.python.org/3.14/library/sys.html#sys._is_immortal) for determining if an object is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal). (Contributed by Peter Bierma in [gh-128509](https://github.com/python/cpython/issues/128509).)

- Under FreeBSD, [`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform) no longer includes the major version number. Its value is consistently `'freebsd'`, in place of `'freebsd13'` or `'freebsd14'`. (Contributed by Michael Osipov in [gh-129393](https://github.com/python/cpython/issues/129393).)

- Raise [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) for [`sys._clear_type_cache()`](https://docs.python.org/3.14/library/sys.html#sys._clear_type_cache). Although this function was marked deprecated back in Python 3.13, it had not been emitting a runtime warning.

- Add [`sys.remote_exec()`](https://docs.python.org/3.14/library/sys.html#sys.remote_exec), which realizes the fresh external debugger interface; consult PEP 768 if you want the full picture. (Pablo Galindo Salgado, Matt Wozniski, and Ivona Stojanovic carried out this work, recorded under [gh-131591](https://github.com/python/cpython/issues/131591).)

- Add the [`sys._jit`](https://docs.python.org/3.14/library/sys.html#sys._jit) namespace, which holds utilities for inspecting just-in-time compilation. (Contributed by Brandt Bucher in [gh-133231](https://github.com/python/cpython/issues/133231).)

[Subject index](INDEX.md) · [Previous source section](symtable.md) · [Next source section](sys-monitoring.md) · [Release/subject declaration](summary-release-highlights.md)
