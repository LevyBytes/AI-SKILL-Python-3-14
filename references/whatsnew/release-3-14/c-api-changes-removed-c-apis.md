# What's new in Python 3.14 / C API changes / Removed C APIs

### Removed C APIs

- Building [`immutable types`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) on top of mutable bases, deprecated back in Python 3.12, now triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). (Contributed by Nikita Sobolev in [gh-119775](https://github.com/python/cpython/issues/119775).)

- Drop the `PyDictObject.ma_version_tag` member, which carried a deprecation in Python 3.12. Rely on the [`PyDict_AddWatcher()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_AddWatcher) API in its place. (Contributed by Sam Gross in [gh-124296](https://github.com/python/cpython/issues/124296).)

- Drop the private `_Py_InitializeMain()` function. It had been a [provisional API](https://docs.python.org/3.14/glossary.html#term-provisional-API) introduced in Python 3.8 via [**PEP 587**](https://peps.python.org/pep-0587/). (Contributed by Victor Stinner in [gh-129033](https://github.com/python/cpython/issues/129033).)

- Drop the undocumented `Py_C_RECURSION_LIMIT` and `PyThreadState.c_recursion_remaining` APIs. Both arrived in 3.13 and have now gone away with no deprecation period. Guard C code against runaway recursion using [`Py_EnterRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_EnterRecursiveCall). (Removed by Petr Viktorin in [gh-133079](https://github.com/python/cpython/issues/133079), see also [gh-130396](https://github.com/python/cpython/issues/130396).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-limited-c-api-changes.md) · [Next source section](c-api-changes-deprecated-c-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md)
