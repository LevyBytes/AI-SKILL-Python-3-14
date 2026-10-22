# Python 3.12.0 alpha 4 / library / functions and types

[gh-100740](https://github.com/python/cpython/issues/100740): Make `unittest.mock.Mock` honor the spec for attribute names that begin with `assert`.

[gh-100690](https://github.com/python/cpython/issues/100690): A `Mock` object that is not unsafe will now raise an `AttributeError` if you read an attribute whose name matches an assertion but lacks the `assert_` prefix ? for instance, reaching for `called_once` rather than `assert_called_once`. The same already occurred for attribute names carrying the prefixes `assert`, `assret`, `asert`, `aseert`, and `assrt`.

[gh-100234](https://github.com/python/cpython/issues/100234): Give the `lambd` parameter of random.expovariate() a default value of 1.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
