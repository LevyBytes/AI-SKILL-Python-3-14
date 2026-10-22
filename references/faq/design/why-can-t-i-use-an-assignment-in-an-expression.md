# Why can't I use an assignment in an expression?

### Why can't I use an assignment in an expression?

As of Python 3.8, you can!

Assignment expressions that use the walrus operator `:=` bind a variable inside an expression:

```python
while chunk := fp.read(200):
   print(chunk)

```

Consult [**PEP 572**](https://peps.python.org/pep-0572/) for further detail.

[Subject index](INDEX.md)
