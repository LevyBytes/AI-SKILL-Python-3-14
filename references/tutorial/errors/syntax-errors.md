# 8.1. Syntax Errors

### 8.1. Syntax Errors

Syntax errors — sometimes called parsing errors — are probably the complaint you'll bump into most often while Python is still new to you:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax

```

The offending line is echoed back by the parser, with small arrows marking the spot where it caught the problem. Keep in mind that this spot isn't necessarily the one you have to correct. Here, the trouble surfaces at the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function, because a colon (`':'`) is absent right ahead of it.

So that you can tell where to look when the input originated from a file, the file name (`<stdin>` here) along with the line number are shown.

[Subject index](INDEX.md) · [Previous source section](errors-and-exceptions.md) · [Following source section](exceptions.md)
