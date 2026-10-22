# Python 3.13.0 alpha 2 / c api / removed

[gh-112026](https://github.com/python/cpython/issues/112026): Reinstate the following removed private C API functions, macros and structures, none of which yet has a straightforward substitute:

  - _PyDict_GetItem_KnownHash()

  - _PyDict_NewPresized()

  - _PyHASH_BITS

  - _PyHASH_IMAG

  - _PyHASH_INF

  - _PyHASH_MODULUS

  - _PyHASH_MULTIPLIER

  - _PyLong_Copy()

  - _PyLong_FromDigits()

  - _PyLong_New()

  - _PyLong_Sign()

  - _PyObject_CallMethodId()

  - _PyObject_CallMethodNoArgs()

  - _PyObject_CallMethodOneArg()

  - _PyObject_CallOneArg()

  - _PyObject_EXTRA_INIT

  - _PyObject_FastCallDict()

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
