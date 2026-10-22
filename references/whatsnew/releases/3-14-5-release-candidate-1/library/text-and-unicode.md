# Python 3.14.5 release candidate 1 / library / text and unicode

[gh-148680](https://github.com/python/cpython/issues/148680): When `ForwardRef` objects hold internal names standing in for known objects, evaluating them as strings now surfaces the known object's `type_repr` in place of the internal `__annotationlib_name_x__` name.

[gh-148192](https://github.com/python/cpython/issues/148192): `email.generator.Generator._make_boundary` might miss a repeated boundary string whenever linesep wasn't n. Repeated boundary strings are now spotted correctly even when linesep is rn.

[gh-145831](https://github.com/python/cpython/issues/145831): Stop `email.quoprimime.decode()` from leaving behind a stray `\r` under `eol='\r\n'`, by trimming the whole *eol* sequence rather than a single character.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
