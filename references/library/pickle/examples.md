# pickle — Examples

### Examples

When you want the most minimal code, reach for the `dump()` and `load()` functions.

```python
import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3+4j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

```

Below, the example loads back the pickled data that was just produced.

```python
import pickle

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)

```

[Subject index](INDEX.md) · [Previous](performance.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
