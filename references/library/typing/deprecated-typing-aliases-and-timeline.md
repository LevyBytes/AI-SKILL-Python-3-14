# Deprecated typing aliases and migration timeline

Deprecated since version 3.9: [`collections.abc.Generator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator) accepts subscripting (`[]`) these days. Consult [**PEP 585**](https://peps.python.org/pep-0585/) along with [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

Changed in version 3.13: Defaults for the send and return types are now available.

`*class *typing.Hashable`

A deprecated alias pointing at [`collections.abc.Hashable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Hashable).

Deprecated since version 3.12: Reach for [`collections.abc.Hashable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Hashable) on its own from now on.

`*class *typing.Reversible(*Iterable[T_co]*)`

A deprecated alias pointing at [`collections.abc.Reversible`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Reversible).

Deprecated since version 3.9: [`collections.abc.Reversible`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Reversible) takes subscripting (`[]`) nowadays. Refer to [**PEP 585**](https://peps.python.org/pep-0585/) together with [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

`*class *typing.Sized`

A deprecated alias pointing at [`collections.abc.Sized`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sized).

Deprecated since version 3.12: Use [`collections.abc.Sized`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sized) directly from here on.

#### Aliases to [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) ABCs

`*class *typing.ContextManager(*Generic[T_co, ExitT_co]*)`

A deprecated alias pointing at [`contextlib.AbstractContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractContextManager).

Here the leading type parameter, `T_co`, stands for whatever the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method gives back. The second type parameter is optional, `ExitT_co`, falling back to `bool | None`, and it stands for whatever the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method gives back.

Added in version 3.5.4.

Deprecated since version 3.9: [`contextlib.AbstractContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractContextManager) now permits subscripting (`[]`). Have a look at [**PEP 585**](https://peps.python.org/pep-0585/) plus [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

Changed in version 3.13: The optional second type parameter, `ExitT_co`, was introduced.

`*class *typing.AsyncContextManager(*Generic[T_co, AExitT_co]*)`

A deprecated alias pointing at [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractAsyncContextManager).

Here the leading type parameter, `T_co`, stands for whatever the [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) method gives back. The second type parameter is optional, `AExitT_co`, falling back to `bool | None`, and it stands for whatever the [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) method gives back.

Added in version 3.6.2.

Deprecated since version 3.9: [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractAsyncContextManager) now permits subscripting (`[]`). Have a look at [**PEP 585**](https://peps.python.org/pep-0585/) plus [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

Changed in version 3.13: The optional second type parameter, `AExitT_co`, was introduced.

### Deprecation Timeline of Major Features

A number of `typing` features are deprecated and could disappear in some later Python release. For your convenience, the table below collects the principal deprecations. Expect this to shift over time, and bear in mind that it does not capture every deprecation.

| Feature | Deprecated in | Projected removal | PEP/issue |
| --- | --- | --- | --- |
| `typing` versions of standard collections | 3.9 | Undecided (consult Deprecated aliases for the details) | **PEP 585** |
| `typing.ByteString` | 3.9 | 3.17 | gh-91896 |
| `typing.Text` | 3.11 | Undecided | gh-92332 |
| `typing.Hashable` and `typing.Sized` | 3.12 | Undecided | gh-94309 |
| `typing.TypeAlias` | 3.12 | Undecided | **PEP 695** |
| `@typing.no_type_check_decorator` | 3.13 | 3.15 | gh-106309 |
| `typing.AnyStr` | 3.13 | 3.18 | gh-105578 |

[Subject index](INDEX.md)
