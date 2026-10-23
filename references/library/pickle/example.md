# pickle - Example

### Example

Below is a minimal example in which we build a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) subclass that can take part in out-of-band buffer pickling:

```python
class ZeroCopyByteArray(bytearray):

    def __reduce_ex__(self, protocol):
        if protocol >= 5:
            return type(self)._reconstruct, (PickleBuffer(self),), None
        else:
            # PickleBuffer is forbidden with pickle protocols <= 4.
            return type(self)._reconstruct, (bytearray(self),)

    @classmethod
    def _reconstruct(cls, obj):
        with memoryview(obj) as m:
            # Get a handle over the original buffer object
            obj = m.obj
            if type(obj) is cls:
                # Original buffer object is a ZeroCopyByteArray, return it
                # as-is.
                return obj
            else:
                return cls(obj)

```

The reconstructor (the `_reconstruct` class method) hands back the buffer's providing object when that object is of the right type. This offers a simple way to mimic zero-copy behaviour in this toy example.

From the consumer's perspective, we may pickle those objects in the ordinary fashion, and unserializing them yields a copy of the original object:

```python
b = ZeroCopyByteArray(b"abc")
data = pickle.dumps(b, protocol=5)
new_b = pickle.loads(data)
print(b == new_b)  # True
print(b is new_b)  # False: a copy was made

```

If instead we supply a *buffer_callback* and then hand the gathered buffers back at unserialization time, we manage to recover the original object:

```python
b = ZeroCopyByteArray(b"abc")
buffers = []
data = pickle.dumps(b, protocol=5, buffer_callback=buffers.append)
new_b = pickle.loads(data, buffers=buffers)
print(b == new_b)  # True
print(b is new_b)  # True: no copy was made

```

A limitation of this example is that [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) owns the memory it allocates: you cannot build a `bytearray` instance backed by some other object's memory. Third-party datatypes such as NumPy arrays, however, are free of this limitation and permit zero-copy pickling (or pickling that makes as few copies as it can) when data moves between separate processes or systems.

See also

[**PEP 574**](https://peps.python.org/pep-0574/) – Pickle protocol 5 with out-of-band data

[Subject index](INDEX.md) · [Previous](consumer-api.md) · [Continue](restricting-globals.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
