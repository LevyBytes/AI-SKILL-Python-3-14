# json`json` - JSON encoder and decoder - Section introduction and initial examples

### `json` - JSON encoder and decoder

**Source code:** [Lib/json/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/json/__init__.py)

---

[JSON (JavaScript Object Notation)](https://json.org) is a compact format for exchanging data that draws on [JavaScript](https://en.wikipedia.org/wiki/JavaScript) object literal notation (though it does not form a strict subset of JavaScript [1] ). Its definition appears in [**RFC 7159**](https://datatracker.ietf.org/doc/html/rfc7159.html) (superseding [**RFC 4627**](https://datatracker.ietf.org/doc/html/rfc4627.html)) and in [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/).

Note

When discussing JSON handling in Python, the word “object” can be confusing. Every Python value is, in fact, an object. Within JSON, however, an object means data enclosed by curly braces, much like a Python dictionary.

Warning

Take care when reading JSON that originates from sources you do not trust. A crafted, hostile JSON string can drive the decoder to use large amounts of CPU and memory. It is wise to cap how much data you allow to be parsed.

The interface presented here will feel familiar to anyone who has worked with the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) and [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) modules from the standard library.

Encoding basic Python object hierarchies:

```python
>>> import json
>>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
>>> print(json.dumps("\"foo\bar"))
"\"foo\bar"
>>> print(json.dumps('\u1234'))
"\u1234"
>>> print(json.dumps('\\'))
"\\"
>>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
{"a": 0, "b": 0, "c": 0}
>>> from io import StringIO
>>> io = StringIO()
>>> json.dump(['streaming API'], io)
>>> io.getvalue()
'["streaming API"]'

```

Compact encoding:

```python
>>> import json
>>> json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
'[1,2,3,{"4":5,"6":7}]'

```

Pretty printing:

```python
>>> import json
>>> print(json.dumps({'6': 7, '4': 5}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}

```

Customizing JSON object encoding:

```python
>>> import json
>>> def custom_json(obj):
...     if isinstance(obj, complex):
...         return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
...     raise TypeError(f'Cannot serialize object of {type(obj)}')
...
>>> json.dumps(1 + 2j, default=custom_json)
'{"__complex__": true, "real": 1.0, "imag": 2.0}'

```

Decoding JSON:

[Subject index](INDEX.md) · [Continue](json-json-encoder-and-decoder-code-example-import-json.md)
