# json — Repeated Names Within an Object

### Repeated Names Within an Object

Although the RFC says the names inside a JSON object ought to be unique, it lays down no rule for how duplicate names in JSON objects must be treated. By default, this module raises no exception; rather, for any repeated name it keeps only the final name-value pair and discards the rest:

```python
>>> weird_json = '{"x": 1, "x": 2, "x": 3}'
>>> json.loads(weird_json)
{'x': 3}

```

You can change this behavior through the *object_pairs_hook* parameter.

[Subject index](INDEX.md) · [Previous](infinite-and-nan-number-values.md) · [Continue](top-level-non-object-non-array-values.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
