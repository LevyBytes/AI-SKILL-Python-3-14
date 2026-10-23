# What's New In Python 3.2 / tempfile - tempfile

### tempfile

A new context manager, [`TemporaryDirectory`](https://docs.python.org/3.14/library/tempfile.html#tempfile.TemporaryDirectory), now lives in the [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile) module, giving you straightforward, deterministic teardown of temporary directories:

```python
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary dir:', tmpdirname)

```

(Contributed by Neil Schemenauer and Nick Coghlan; [bpo-5178](https://bugs.python.org/issue?@action=redirect&bpo=5178).)

[Subject index](INDEX.md) · [Previous source section](asyncore.md) · [Next source section](inspect.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
