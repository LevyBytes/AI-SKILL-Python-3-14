# Python 3.14.0 alpha 1 / core and builtins / functions

[gh-122234](https://github.com/python/cpython/issues/122234): The float and complex specializations feeding [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) now rely on compensated summation everywhere. And, for integer items inside those same specializations: [`PyLong_AsDouble()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsDouble) takes over from [`PyLong_AsLongAndOverflow()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLongAndOverflow). Sergey B Kirpichev contributed the patch.

[gh-119180](https://github.com/python/cpython/issues/119180): [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) and [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) now wrap their underlying callable's [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) and [`__annotate__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotate__) attributes lazily. Consult [**PEP 649**](https://peps.python.org/pep-0649/). Jelle Zijlstra contributed the patch.

[gh-123271](https://github.com/python/cpython/issues/123271): Allow several iterations sharing one [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) iterator to run safely while free-threading.

[gh-121149](https://github.com/python/cpython/issues/121149): Added a specialization for summing complexes, which also raises the accuracy of builtin [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) on those inputs. Sergey B Kirpichev contributed the patch.

[gh-119740](https://github.com/python/cpython/issues/119740): Drop the formerly-deprecated path that let [`int()`](https://docs.python.org/3.14/library/functions.html#int) fall back to [`__trunc__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__trunc__).

[gh-109218](https://github.com/python/cpython/issues/109218): A string handed to [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) is now accepted only positionally. Handing a complex number as the ?real? or ?imag? argument has become deprecated; supply it instead as one lone positional argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
