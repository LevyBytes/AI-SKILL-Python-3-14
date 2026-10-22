# 4.2.6. Interaction with dynamic features

### 4.2.6. Interaction with dynamic features

Free variables get their names resolved at runtime rather than at compile time. Because of that, the code below will print 42:

```python
i = 10
def f():
    print(i)
i = 42
f()

```

The [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) and [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) functions lack access to the complete environment when resolving names. The caller's local and global namespaces are where names may be resolved. Free variables get resolved not in the nearest enclosing namespace but in the global namespace. [1] Both the `exec()` and `eval()` functions accept optional arguments for overriding the global and local namespace. Supply just one namespace and it serves for both.

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Owning language section](binding-of-names.md) · [Previous source section](builtins-and-restricted-execution.md) · [Following source section](exceptions.md)
