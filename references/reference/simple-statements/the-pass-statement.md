# 7.4. The `pass` statement

### 7.4. The `pass` statement

```text

pass_stmt: "pass"
```

`pass` is a null operation ? running it makes nothing happen. It comes in handy as a placeholder wherever a statement is syntactically required but no code has to run, as in:

```python
def f(arg): pass    # a function that does nothing (yet)

class C: pass       # a class with no methods (yet)

```

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-assert-statement.md) · [Following source section](the-del-statement.md)
