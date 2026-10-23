# json - Infinite and NaN Number Values

### Infinite and NaN Number Values

Representing infinite or NaN number values is something the RFC disallows. Even so, by default this module reads and writes `Infinity`, `-Infinity`, and `NaN` as though they were legitimate JSON numeric literals:

```python
>>> # Neither of these calls raises an exception, but the results are not valid JSON
>>> json.dumps(float('-inf'))
'-Infinity'
>>> json.dumps(float('nan'))
'NaN'
>>> # Same when deserializing
>>> json.loads('-Infinity')
-inf
>>> json.loads('NaN')
nan

```

On the serializing side, the *allow_nan* parameter lets you change this behavior. On the deserializing side, the *parse_constant* parameter serves that purpose.

[Subject index](INDEX.md) · [Previous](character-encodings.md) · [Continue](repeated-names-within-an-object.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
