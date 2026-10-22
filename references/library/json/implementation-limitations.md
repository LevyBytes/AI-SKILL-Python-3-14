# json — Implementation Limitations

### Implementation Limitations

Certain JSON deserializer implementations might cap things such as:

- how large a JSON text they will accept

- how deeply JSON objects and arrays are allowed to nest

- the span and precision permitted for JSON numbers

- what JSON strings may contain and how long they can run

No such caps are applied by this module beyond whatever the corresponding Python datatypes or the Python interpreter already enforce.

As you serialize to JSON, keep an eye on limits like these in whatever applications will read your JSON. A frequent pitfall is that JSON numbers get parsed into IEEE 754 double precision values, inheriting the range and precision bounds of that format. This matters most when you serialize Python [`int`](https://docs.python.org/3.14/library/functions.html#int) values of enormous magnitude, or when you serialize objects of less common numeric types like [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal).

[Subject index](INDEX.md) · [Previous](top-level-non-object-non-array-values.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
