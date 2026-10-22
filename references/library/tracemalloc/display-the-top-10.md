# tracemalloc — Display the top 10

### Examples

### Display the top 10

Show the 10 files responsible for the largest allocations:

```python
import tracemalloc

tracemalloc.start()

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

```

Sample output produced while running the Python test suite:

```python
[ Top 10 ]
<frozen importlib._bootstrap>:716: size=4855 KiB, count=39328, average=126 B
<frozen importlib._bootstrap>:284: size=521 KiB, count=3199, average=167 B
/usr/lib/python3.4/collections/__init__.py:368: size=244 KiB, count=2315, average=108 B
/usr/lib/python3.4/unittest/case.py:381: size=185 KiB, count=779, average=243 B
/usr/lib/python3.4/unittest/case.py:402: size=154 KiB, count=378, average=416 B
/usr/lib/python3.4/abc.py:133: size=88.7 KiB, count=347, average=262 B
<frozen importlib._bootstrap>:1446: size=70.4 KiB, count=911, average=79 B
<frozen importlib._bootstrap>:1454: size=52.0 KiB, count=25, average=2131 B
<string>:5: size=49.7 KiB, count=148, average=344 B
/usr/lib/python3.4/sysconfig.py:411: size=48.0 KiB, count=1, average=48.0 KiB

```

The output reveals that Python pulled in `4855 KiB` of data (bytecode and constants) from modules, while the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module used `244 KiB` constructing [`namedtuple`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) types.

Consult `Snapshot.statistics()` for additional options.

[Subject index](INDEX.md) · [Continue](compute-differences.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md)
