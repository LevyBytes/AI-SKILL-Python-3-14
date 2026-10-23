# Thread safety for set objects - Code example: s.isdisjoint(other)          # both locked

```python
s.isdisjoint(other)          # both locked
s.issubset(other)            # both locked
s.issuperset(other)          # both locked

```

Operations spanning multiple accesses, iteration included, are never atomic:

```python
# NOT atomic: check-then-act
if elem in s:
      s.remove(elem)

# NOT thread-safe: iteration while modifying
for elem in s:
      process(elem)  # another thread may modify s

```

Reach for external synchronization whenever [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) instances are shared between threads. Refer to [Python support for free threading](https://docs.python.org/3.14/howto/free-threading-python.html#freethreading-python-howto) for further detail.

[Subject index](INDEX.md) · [Previous](set-thread-safety-overview.md) · [Continue](thread-safety-for-bytearray-objects.md) · [Owning module, declaration or section: Thread safety for set objects](set-thread-safety-overview.md)
