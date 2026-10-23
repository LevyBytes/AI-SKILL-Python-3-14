# What’s New in Python 2.6 / The `json` module: JavaScript Object Notation - json

### The [`json`](https://docs.python.org/3.14/library/json.html#module-json) module: JavaScript Object Notation

Encoding and decoding Python values to and from JSON (Javascript Object Notation) is handled by the freshly added [`json`](https://docs.python.org/3.14/library/json.html#module-json) module. JSON is a compact interchange format that web applications lean on frequently. Further details on JSON live at [http://www.json.org](http://www.json.org).

Out of the box, [`json`](https://docs.python.org/3.14/library/json.html#module-json) can decode and encode the bulk of Python's built-in types. Here is a dictionary being encoded and then decoded:

```python
>>> import json
>>> data = {"spam": "foo", "parrot": 42}
>>> in_json = json.dumps(data) # Encode the data
>>> in_json
'{"parrot": 42, "spam": "foo"}'
>>> json.loads(in_json) # Decode into a Python object
{"spam": "foo", "parrot": 42}

```

You can additionally roll your own decoders and encoders to cover further types. The module also supports pretty-printing of the JSON strings.

[`json`](https://docs.python.org/3.14/library/json.html#module-json) (which began life as simplejson) was authored by Bob Ippolito.

[Subject index](INDEX.md) · [Previous source section](the-future-builtins-module.md) · [Next source section](the-plistlib-module-a-property-list-parser.md) · [Release/subject declaration](python-3-0.md)
