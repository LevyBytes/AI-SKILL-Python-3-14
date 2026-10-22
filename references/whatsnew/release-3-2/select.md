# What's New In Python 3.2 / select — select

### select

A new constant attribute, [`PIPE_BUF`](https://docs.python.org/3.14/library/select.html#select.PIPE_BUF), is now published by the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module; it states the smallest byte count that is assured not to block once [`select.select()`](https://docs.python.org/3.14/library/select.html#select.select) reports a pipe as writable.

```python
>>> import select
>>> select.PIPE_BUF
512

```

(Available on Unix systems. Patch by Sébastien Sabl? in [bpo-9862](https://bugs.python.org/issue?@action=redirect&bpo=9862))

[Subject index](INDEX.md) · [Previous source section](popen.md) · [Next source section](gzip-and-zipfile.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
