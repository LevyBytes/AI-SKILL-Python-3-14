# Borrowed References

### Borrowed References

A number of C API calls give back [borrowed references](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). Such calls cease to be thread-safe the moment the enclosing object is changed by another thread. As a case in point, leaning on [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem) is risky whenever the list might be altered concurrently.

Below is a table pairing several borrowed-reference calls with the substitutes that instead yield [strong references](https://docs.python.org/3.14/glossary.html#term-strong-reference).

| Borrowed reference API | Strong reference API |
| --- | --- |
| `PyList_GetItem()` | `PyList_GetItemRef()` |
| `PyList_GET_ITEM()` | `PyList_GetItemRef()` |
| `PyDict_GetItem()` | `PyDict_GetItemRef()` |
| `PyDict_GetItemWithError()` | `PyDict_GetItemRef()` |
| `PyDict_GetItemString()` | `PyDict_GetItemStringRef()` |
| `PyDict_SetDefault()` | `PyDict_SetDefaultRef()` |
| `PyDict_Next()` | none (see PyDict_Next) |
| `PyWeakref_GetObject()` | `PyWeakref_GetRef()` |
| `PyWeakref_GET_OBJECT()` | `PyWeakref_GetRef()` |
| `PyImport_AddModule()` | `PyImport_AddModuleRef()` |
| `PyCell_GET()` | `PyCell_Get()` |

Borrowed-reference calls are not uniformly dangerous. Take [`PyTuple_GetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_GetItem): it poses no hazard precisely because tuples cannot be mutated. By the same token, the calls above are not always misused. Consider [`PyDict_GetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItem), commonly applied to unpack keyword-argument dictionaries during a function call; because those dictionaries stay effectively private and out of reach of other threads, borrowing a reference there is perfectly fine.

A few of the replacement functions first appeared in Python 3.13. To get working versions of them on earlier Python releases, pull in the [pythoncapi-compat](https://github.com/python/pythoncapi-compat) package.

[Subject index](INDEX.md) · [Previous source context](pydict-next.md) · [Following source context](memory-allocation-apis.md)
