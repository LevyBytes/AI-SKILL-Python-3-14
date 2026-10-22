# tracemalloc — Compute differences

### Compute differences

Grab two snapshots and report what changed between them:

```python
import tracemalloc
tracemalloc.start()
# ... start your application ...

snapshot1 = tracemalloc.take_snapshot()
# ... call the function leaking memory ...
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)

```

Sample output captured before and after exercising part of the Python test suite:

```python
[ Top 10 differences ]
<frozen importlib._bootstrap>:716: size=8173 KiB (+4428 KiB), count=71332 (+39369), average=117 B
/usr/lib/python3.4/linecache.py:127: size=940 KiB (+940 KiB), count=8106 (+8106), average=119 B
/usr/lib/python3.4/unittest/case.py:571: size=298 KiB (+298 KiB), count=589 (+589), average=519 B
<frozen importlib._bootstrap>:284: size=1005 KiB (+166 KiB), count=7423 (+1526), average=139 B
/usr/lib/python3.4/mimetypes.py:217: size=112 KiB (+112 KiB), count=1334 (+1334), average=86 B
/usr/lib/python3.4/http/server.py:848: size=96.0 KiB (+96.0 KiB), count=1 (+1), average=96.0 KiB
/usr/lib/python3.4/inspect.py:1465: size=83.5 KiB (+83.5 KiB), count=109 (+109), average=784 B
/usr/lib/python3.4/unittest/mock.py:491: size=77.7 KiB (+77.7 KiB), count=143 (+143), average=557 B
/usr/lib/python3.4/urllib/parse.py:476: size=71.8 KiB (+71.8 KiB), count=969 (+969), average=76 B
/usr/lib/python3.4/contextlib.py:38: size=67.2 KiB (+67.2 KiB), count=126 (+126), average=546 B

```

Here Python has brought in `8173 KiB` of module data (bytecode and constants), which is `4428 KiB` beyond what was present at the time of the earlier snapshot, taken before the tests ran. In the same way, the [`linecache`](https://docs.python.org/3.14/library/linecache.html#module-linecache) module has stored `940 KiB` of Python source so it can render tracebacks, every byte of which has appeared since the previous snapshot.

When free memory is scarce, you can persist snapshots to disk with the `Snapshot.dump()` method and study them later offline. Afterward, the `Snapshot.load()` method reload the snapshot.

[Subject index](INDEX.md) · [Previous](display-the-top-10.md) · [Continue](get-the-traceback-of-a-memory-block.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md)
