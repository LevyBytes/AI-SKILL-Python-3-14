# 9.2.1. Scopes and Namespaces Example

### 9.2.1. Scopes and Namespaces Example

Here is an example showing how to reach the various scopes and namespaces, and how [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) and [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) influence the binding of a variable:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

```

Running the example code produces:

```none
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam

```

Observe how the *local* assignment (which is the default) left *scope_test*'s binding of *spam* untouched. The [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) assignment altered *scope_test*'s binding of *spam*, while the [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) assignment altered the binding at module level.

Notice too that *spam* had no binding at all prior to the [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) assignment.

[Subject index](INDEX.md) · [Previous source section](python-scopes-and-namespaces.md) · [Following source section](a-first-look-at-classes.md)
