# tomllib — `tomllib` — Parse TOML files

## tomllib — Parse TOML files

### `tomllib` — Parse TOML files

Added in version 3.11.

**Source code:** [Lib/tomllib](https://github.com/python/cpython/tree/3.14/Lib/tomllib)

---

What this module offers is an interface that parses TOML 1.0.0 (Tom's Obvious Minimal Language, [https://toml.io](https://toml.io/en/)). Writing TOML is not something this module handles.

Warning

Take care when you parse data coming from untrusted sources. A hostile TOML string could push the decoder into burning through sizable CPU and memory. The advice is to cap how much data you hand it for parsing.

See also

The [Tomli-W package](https://pypi.org/project/tomli-w/) is a TOML writer you can pair with this module, offering a write API that will feel familiar to anyone who has used the standard library [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) and [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) modules.

See also

The [TOML Kit package](https://pypi.org/project/tomlkit/) is a style-preserving TOML library that can both read and write. For editing TOML files that already exist, it is the recommended stand-in for this module.

The functions this module defines are:

 tomllib.load(*fp*, */*, ***, *parse_float=float*)

Read a TOML file. Pass a readable binary file object as the first argument. Give back a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). TOML types map onto Python via this conversion table.

*parse_float* gets invoked with the string of every TOML float awaiting decoding. By default this matches `float(num_str)`. You can use it to swap in a different datatype or parser for TOML floats (for example [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)). The callable must not give back a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) or a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), or else a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised.

A `TOMLDecodeError` will be raised on an invalid TOML document.

 tomllib.loads(*s*, */*, ***, *parse_float=float*)

Load TOML out of a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object. Give back a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). TOML types map onto Python via this conversion table. The *parse_float* argument keeps the same meaning it holds in `load()`.

A `TOMLDecodeError` will be raised on an invalid TOML document.

The exceptions on offer are:

 *exception *tomllib.TOMLDecodeError(*msg*, *doc*, *pos*)

A subclass of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) carrying these extra attributes:

 msg

The unformatted error message.

 doc

The TOML document being parsed.

 pos

The index of *doc* where parsing failed.

 lineno

The line corresponding to *pos*.

 colno

The column corresponding to *pos*.

Changed in version 3.14: Introduced the *msg*, *doc* and *pos* parameters, along with the `msg`, `doc`, `pos`, `lineno` and `colno` attributes.

Deprecated since version 3.14: Passing free-form positional arguments is deprecated.

[Subject index](INDEX.md) · [Continue](examples.md)
