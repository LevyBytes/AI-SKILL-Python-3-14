# Python 3.14.0 alpha 5 / c api / init config

[gh-129033](https://github.com/python/cpython/issues/129033): Took out the `_PyInterpreterState_GetConfigCopy()` and `_PyInterpreterState_SetConfig()` private functions. Reach instead for [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) and [`PyConfig_Set()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Set), the public C API that [**PEP 741**](https://peps.python.org/pep-0741/) "Python Configuration C API" brought in. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
