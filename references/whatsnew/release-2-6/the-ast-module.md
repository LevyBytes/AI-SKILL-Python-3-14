# What’s New in Python 2.6 / The `ast` module - ast

### The [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module

An Abstract Syntax Tree view of Python source is exposed by the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module, and Armin Ronacher added a collection of helper functions that cover a range of frequent chores. Anything that processes Python source — HTML templating libraries, code analyzers, and the like — should find them handy.

An expression goes into `parse()`, which hands back an AST. To inspect a tree while debugging, `dump()` renders it as a printable representation:

```python
import ast

t = ast.parse("""
d = {}
for i in 'abcdefghijklm':
    d[i + i] = ord(i) - ord('a') + 1
print d
""")
print ast.dump(t)

```

The result is a tree nested many levels deep:

```python
Module(body=[
  Assign(targets=[
    Name(id='d', ctx=Store())
   ], value=Dict(keys=[], values=[]))
  For(target=Name(id='i', ctx=Store()),
      iter=Str(s='abcdefghijklm'), body=[
    Assign(targets=[
      Subscript(value=
        Name(id='d', ctx=Load()),
          slice=
          Index(value=
            BinOp(left=Name(id='i', ctx=Load()), op=Add(),
             right=Name(id='i', ctx=Load()))), ctx=Store())
     ], value=
     BinOp(left=
      BinOp(left=
       Call(func=
        Name(id='ord', ctx=Load()), args=[
          Name(id='i', ctx=Load())
         ], keywords=[], starargs=None, kwargs=None),
       op=Sub(), right=Call(func=
        Name(id='ord', ctx=Load()), args=[
          Str(s='a')
         ], keywords=[], starargs=None, kwargs=None)),
       op=Add(), right=Num(n=1)))
    ], orelse=[])
   Print(dest=None, values=[
     Name(id='d', ctx=Load())
   ], nl=True)
 ])

```

Give `literal_eval()` either a string or an AST that stands for a literal expression; it parses that input, evaluates it, and hands back the value. By "literal expression" we mean a Python expression made solely of strings, numbers, dictionaries, and so on, with no statements or function calls anywhere. Whenever you must evaluate an expression yet cannot tolerate the security exposure of an [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) call, `literal_eval()` does the job without that danger:

```python
>>> literal = '("a", "b", {2:4, 3:8, 1:2})'
>>> print ast.literal_eval(literal)
('a', 'b', {1: 2, 2: 4, 3: 8})
>>> print ast.literal_eval('"a" + "b"')
Traceback (most recent call last):
  ...
ValueError: malformed string

```

Beyond that, the module ships `NodeVisitor` and `NodeTransformer` classes for walking through and rewriting an AST, plus functions covering ordinary transformations such as adjusting line numbers.

[Subject index](INDEX.md) · [Previous source section](new-and-improved-modules-unpack-all-the-files-in-the-archive.md) · [Next source section](the-future-builtins-module.md) · [Release/subject declaration](python-3-0.md)
