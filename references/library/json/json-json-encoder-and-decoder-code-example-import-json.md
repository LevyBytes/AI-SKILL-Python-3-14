# json — `json` — JSON encoder and decoder — Code example: >>> import json

```python
>>> import json
>>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
['foo', {'bar': ['baz', None, 1.0, 2]}]
>>> json.loads('"\\"foo\\bar"')
'"foo\x08ar'
>>> from io import StringIO
>>> io = StringIO('["streaming API"]')
>>> json.load(io)
['streaming API']

```

Customizing JSON object decoding:

```python
>>> import json
>>> def as_complex(dct):
...     if '__complex__' in dct:
...         return complex(dct['real'], dct['imag'])
...     return dct
...
>>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
...     object_hook=as_complex)
(1+2j)
>>> import decimal
>>> json.loads('1.1', parse_float=decimal.Decimal)
Decimal('1.1')

```

Extending `JSONEncoder`:

```python
>>> import json
>>> class ComplexEncoder(json.JSONEncoder):
...     def default(self, obj):
...         if isinstance(obj, complex):
...             return [obj.real, obj.imag]
...         # Let the base class default method raise the TypeError
...         return super().default(obj)
...
>>> json.dumps(2 + 1j, cls=ComplexEncoder)
'[2.0, 1.0]'
>>> ComplexEncoder().encode(2 + 1j)
'[2.0, 1.0]'
>>> list(ComplexEncoder().iterencode(2 + 1j))
['[2.0', ', 1.0', ']']

```

Using `json` from the shell to validate and pretty-print:

```shell
$ echo '{"json":"obj"}' | python -m json
{
    "json": "obj"
}
$ echo '{1.2:3.4}' | python -m json
Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

```

See Command-line interface for detailed documentation.

Note

Every JSON text is also valid [YAML](https://yaml.org/) 1.2. With its default configuration — notably the default *separators* value — the output of this module additionally qualifies as a subset of YAML 1.0 and 1.1. Consequently, you can treat this module as a YAML serializer too.

Note

By default, the encoders and decoders here keep the ordering of both their input and their output. The only way ordering disappears is when the containers underneath are themselves unordered.

[Subject index](INDEX.md) · [Previous](json-encoding-and-decoding-overview.md) · [Continue](json-dump-to-json-dumps.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
