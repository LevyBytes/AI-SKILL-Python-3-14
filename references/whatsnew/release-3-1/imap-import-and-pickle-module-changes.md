# What’s New In Python 3.1 / New, Improved, and Deprecated Modules - imaplib, importlib, pickle

```python
>>> sys.version_info
sys.version_info(major=3, minor=1, micro=0, releaselevel='alpha', serial=2)

```

(Contributed by Ross Light; [bpo-4285](https://bugs.python.org/issue?@action=redirect&bpo=4285).)

- IPv6 is now supported by the `nntplib` and [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) modules.

(Contributed by Derek Morr; [bpo-1655](https://bugs.python.org/issue?@action=redirect&bpo=1655) and [bpo-1664](https://bugs.python.org/issue?@action=redirect&bpo=1664).)

- To work better alongside Python 2.x at protocol 2 or below, the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module was reworked. Reshuffling the standard library shifted the canonical reference for plenty of objects. To illustrate, what Python 2 calls `__builtin__.set` goes by `builtins.set` in Python 3. That divergence got in the way of moving data between Python versions. Yet now, with protocol 2 or below in effect, the pickler reaches for the legacy Python 2 names automatically whether loading or dumping. By default this remapping is switched on, though the *fix_imports* option lets you turn it off:

```python
>>> s = {1, 2, 3}
>>> pickle.dumps(s, protocol=0)
b'c__builtin__\nset\np0\n((lp1\nL1L\naL2L\naL3L\natp2\nRp3\n.'
>>> pickle.dumps(s, protocol=0, fix_imports=False)
b'cbuiltins\nset\np0\n((lp1\nL1L\naL2L\naL3L\natp2\nRp3\n.'

```

One regrettable yet unavoidable consequence here is that protocol 2 pickles made by Python 3.1 cannot be read by Python 3.0. For shuttling data among Python 3.x builds, lean on the newest pickle protocol, protocol 3, since it makes no effort to stay compatible with Python 2.x.

(Contributed by Alexandre Vassalotti and Antoine Pitrou, [bpo-6137](https://bugs.python.org/issue?@action=redirect&bpo=6137).)

- A fresh module, [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib), was added. It delivers a full, portable, pure Python reference implementation of the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement plus its companion, the [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function. It marks a meaningful advance in documenting and pinning down what happens while imports run.

(Contributed by Brett Cannon.)

[Subject index](INDEX.md) · [Previous source section](io-logging-debugging-and-testing-module-changes.md) · [Next source section](optimizations.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md) · [Release/subject declaration](standard-library-module-changes.md)
