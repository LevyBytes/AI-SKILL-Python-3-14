# What's new in Python 3.14 / C API changes / Python configuration C API

### C API changes

### Python configuration C API

Introduce a [PyInitConfig C API](https://docs.python.org/3.14/c-api/init_config.html#pyinitconfig-api) for setting up Python initialization without depending on C structures, leaving room to make ABI-compatible adjustments down the road.

Round out the [**PEP 587**](https://peps.python.org/pep-0587/) [PyConfig C API](https://docs.python.org/3.14/c-api/init_config.html#pyconfig-api) by introducing [`PyInitConfig_AddModule()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_AddModule), which serves to register a built-in extension module; this capability used to go by the name ?inittab?.

Introduce the [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) and [`PyConfig_Set()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Set) functions for reading and writing the current runtime configuration.

[**PEP 587**](https://peps.python.org/pep-0587/) ?Python Initialization Configuration? brought together every approach to setting up Python's initialization. This PEP further consolidates the configuration of Python's preinitialization and initialization beneath one API. On top of that, this PEP narrows embedding Python to a single option rather than the dual ?Python? and ?Isolated? choices (PEP 587), trimming the API further.

For situations that intentionally couple more tightly to CPython implementation details (such as reproducing the complete behavior of CPython’s CLI, configuration mechanisms included), the lower level PEP 587 PyConfig API is still on offer.

(Contributed by Victor Stinner in [gh-107954](https://github.com/python/cpython/issues/107954).)

See also

[**PEP 741**](https://peps.python.org/pep-0741/) and [**PEP 587**](https://peps.python.org/pep-0587/)

[Subject index](INDEX.md) · [Previous source section](pseudo-instructions.md) · [Next source section](c-api-additions.md) · [Release/subject declaration](summary-release-highlights.md)
