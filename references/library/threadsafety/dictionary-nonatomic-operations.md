# Thread safety for dict objects — Code example: d[key] = d[key] + 1

```python
# NOT atomic: read-modify-write
d[key] = d[key] + 1

# NOT atomic: check-then-act (TOCTOU)
if key in d:
    del d[key]

# NOT thread-safe: iteration while modifying
for key, value in d.items():
    process(key)  # another thread may modify d

```

So as to dodge time-of-check to time-of-use (TOCTOU) trouble, lean on atomic operations or catch exceptions:

```python
# Use pop() with default instead of check-then-delete
d.pop(key, None)

# Or handle the exception
try:
    del d[key]
except KeyError:
    pass

```

To iterate safely over a dictionary that another thread might edit, walk a copy instead:

```python
# Make a copy to iterate safely
for key, value in d.copy().items():
    process(key)

```

Reach for external synchronization whenever [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) instances are shared between threads.

[Subject index](INDEX.md) · [Previous](dictionary-thread-safety-overview.md) · [Continue](set-thread-safety-overview.md) · [Owning module, declaration or section: Thread safety for dict objects](dictionary-thread-safety-overview.md)
