# Why don't my signal handlers work?

### Why don't my signal handlers work?

By far the usual culprit is a signal handler declared with the wrong argument list. The handler is invoked as

```python
handler(signum, frame)

```

and therefore needs to be declared taking two parameters:

```python
def handler(signum, frame):
    ...

```

[Subject index](INDEX.md)
