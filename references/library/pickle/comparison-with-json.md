# pickle - Comparison with `json`

### Comparison with `json`

The pickle protocols and [JSON (JavaScript Object Notation)](https://json.org) differ in fundamental ways:

- JSON is a text serialization format (it emits unicode text, though most of the time that is then encoded to `utf-8`), whereas pickle is a binary serialization format;

- JSON is human-readable, while pickle is not;

- JSON is interoperable and sees wide use beyond the Python ecosystem, whereas pickle is Python-specific;

- By default, JSON covers only a portion of the Python built-in types and no custom classes at all; pickle handles a vast assortment of Python types (a great many of them automatically, via clever use of Python's introspection facilities, while harder cases can be addressed by implementing specific object APIs);

- Unlike pickle, deserializing untrusted JSON does not by itself open an arbitrary-code-execution vulnerability.

See also

The [`json`](https://docs.python.org/3.14/library/json.html#module-json) module: a standard library module allowing JSON serialization and deserialization.

[Subject index](INDEX.md) · [Previous](comparison-with-marshal.md) · [Continue](data-stream-format.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
