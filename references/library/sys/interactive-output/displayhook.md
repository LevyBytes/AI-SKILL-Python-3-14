# sys.displayhook

sys.displayhook(*value*)

When *value* is not `None`, this function writes `repr(value)` to `sys.stdout` and stores *value* in `builtins._`. Should `repr(value)` not be encodable to `sys.stdout.encoding` under the `sys.stdout.errors` error handler (which is most likely `'strict'`), it is encoded to `sys.stdout.encoding` using the `'backslashreplace'` error handler instead.

`sys.displayhook` runs against the result of evaluating an [expression](https://docs.python.org/3.14/glossary.html#term-expression) typed into an interactive Python session. You can customize how these values get displayed by assigning a different one-argument function to `sys.displayhook`.

Pseudo-code:

```python
def displayhook(value):
    if value is None:
        return
    # Set '_' to None to avoid recursion
    builtins._ = None
    text = repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    builtins._ = value

```

Changed in version 3.2: Use `'backslashreplace'` error handler on [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError).

[API family](INDEX.md) · [sys context index](../INDEX.md).
