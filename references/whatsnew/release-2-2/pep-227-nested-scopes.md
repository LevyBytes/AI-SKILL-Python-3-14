# What’s New in Python 2.2 / PEP 227: Nested Scopes

### PEP 227: Nested Scopes

Python 2.1 introduced statically nested scopes as an opt-in feature, switched on with a `from __future__ import nested_scopes` directive. Come 2.2, nested scopes need no special activation and are simply always in place. What follows in this section reproduces my account of nested scopes from the “What’s New in Python 2.1” document; if you already went through it back when 2.1 shipped, you may skip ahead past the rest of this section.

The biggest change rolled out in Python 2.1, then rounded out in 2.2, concerns Python’s scoping rules. Under Python 2.0, no more than three namespaces are ever in play when resolving a variable name: the local one, the module-level one, and the built-in one. That regularly caught people off guard, since it clashed with what they instinctively expected. A nested recursive function definition, for one, simply fails:

```python
def f():
    ...
    def g(value):
        ...
        return g(value-1) + 1
    ...

```

The function `g()` is bound to throw a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exception every time, because the name `g` is bound neither in its own local namespace nor in the module-level one. In day-to-day work that rarely bites (how frequently do you define inner functions recursively this way?), yet it also made the [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expression more awkward to use, and that did genuinely sting. Code that leans on `lambda` often shows local variables being smuggled in as the default values of arguments.

```python
def find(self, name):
    "Return list of any entries equal to 'name'"
    L = filter(lambda x, name=name: x == name,
               self.list_attribute)
    return L

```

Code authored in a heavily functional Python style pays a steep readability price for this.

Python 2.2’s headline change is the introduction of static scoping into the language, which clears up this trouble. One immediate consequence is that the `name=name` default argument is no longer needed in the example just shown. Stated plainly: whenever a function never assigns a value to a given variable name (through an assignment, or via the [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def), [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class), or [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statements), references to that name are resolved in the local namespace of the surrounding scope. The PEP carries a fuller rundown of the rules along with a walkthrough of the implementation.

For code that reuses one variable name simultaneously at module level and as a local inside a function holding further function definitions, this change might bring on a few compatibility headaches. That scenario looks fairly improbable, though, since code like that would already have been pretty baffling to read to begin with.

A by-product of the change is that the `from module import *` and `exec` statements now count as illegal inside a function scope under certain circumstances. Although the Python reference manual has always stated that `from module import *` is permitted only at a module’s top level, the CPython interpreter never used to enforce it. While putting nested scopes in place, the compiler that translates Python source into bytecodes must emit different code to reach variables sitting in an enclosing scope. Both `from module import *` and `exec` rob the compiler of any way to work this out, since they introduce names into the local namespace that cannot be known at compile time. Consequently, when a function holds function definitions or [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expressions carrying free variables, the compiler signals the problem by throwing a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exception.

An example will sharpen the explanation above:

```python
x = 1
def f():
    # The next line is a syntax error
    exec 'x=2'
    def g():
        return x

```

Line 4, the one with the `exec` statement, is a syntax error: `exec` would create a new local variable called `x` whose value `g()` ought to read.

That ought not constrain much, given how seldom `exec` appears in typical Python code (and where it does appear, it tends to flag a weak design anyway).

See also

[**PEP 227**](https://peps.python.org/pep-0227/) - Statically Nested Scopes

Authored and implemented by Jeremy Hylton.

[Subject index](INDEX.md) · [Previous source section](unicode-changes.md) · [Next source section](new-and-improved-modules.md) · [Release/subject declaration](introduction.md)
