# pickle`pickle` - Python object serialization

### `pickle` - Python object serialization

**Source code:** [Lib/pickle.py](https://github.com/python/cpython/tree/3.14/Lib/pickle.py)

---

Binary protocols for serializing and de-serializing a Python object structure are what the `pickle` module implements. *"Pickling"* names the process by which a Python object hierarchy gets turned into a byte stream, and *"unpickling"* is the reverse: a byte stream (drawn from a [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file) or a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) is turned back into an object hierarchy. Pickling (and unpickling) also goes by the names "serialization", "marshalling," [1] or "flattening"; to keep things clear, though, the terms used here are "pickling" and "unpickling".

Warning

The `pickle` module **is not secure**. Only unpickle data you trust.

Malicious pickle data can be crafted so that it will **execute arbitrary code during unpickling**. Do not ever unpickle data whose origin might be untrusted, or that might have been altered.

To confirm that data has not been altered, think about signing it with [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac).

When you are dealing with untrusted data, a safer serialization format such as [`json`](https://docs.python.org/3.14/library/json.html#module-json) may suit you better. See Comparison with json.

[Subject index](INDEX.md) · [Continue](comparison-with-marshal.md)
