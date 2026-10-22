# What’s New in Python 2.1 / PEP 227: Nested Scopes

### PEP 227: Nested Scopes

The biggest revision in Python 2.1 affects how Python resolves scopes. Back in Python 2.0, no more than three namespaces are ever consulted when resolving a variable name at any moment: the local one, the module-level one, and the built-in one. Many found this counterintuitive because it clashed with what they naturally assumed. Take a recursive function nested inside another — it simply fails:

```python
def f():
    ...
    def g(value):
        ...
        return g(value-1) + 1
    ...

```

Calling the function `g()` will invariably trigger a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exception, since the name `g` is bound in neither its own local namespace nor at the module level. In day-to-day work this rarely bites you (after all, how frequently do you nest a recursive interior function this way?), yet it also made working with the [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expression more awkward, and that genuinely caused trouble. With `lambda`-based code you’ll routinely see local variables smuggled in as the default values of arguments.

```python
def find(self, name):
    "Return list of any entries equal to 'name'"
    L = filter(lambda x, name=name: x == name,
               self.list_attribute)
    return L

```

Because of this, Python code authored in a heavily functional manner becomes far harder to read.

To remedy this, the headline change in Python 2.1 is the addition of static scoping to the language. The first consequence is that the `name=name` default argument in the example above is no longer required. In short: whenever a particular variable name receives no value inside a function (whether via assignment, or through the [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def), [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class), or [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statements), any reference to it falls through to the local namespace of the surrounding scope. The PEP lays out the rules with more precision and walks through how the implementation works.

For code that reuses one variable name both at module level and as a local inside a function holding further nested function definitions, this revision could introduce compatibility headaches. That scenario seems improbable, though, given that such code would have been fairly confusing to read to begin with.

A consequence of the change is that, in certain situations, the `from module import *` and `exec` statements are now forbidden within a function scope. Although the Python reference manual has long stated that `from module import *` is permitted only at a module’s top level, the CPython interpreter had never policed this until now. Implementing nested scopes forces the compiler — the piece that converts Python source into bytecodes — to emit distinct code for reaching variables in an enclosing scope. Both `from module import *` and `exec` defeat the compiler’s analysis, since they introduce names into the local namespace that cannot be known when compilation happens. Consequently, should a function hold function definitions or [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expressions that reference free variables, the compiler signals the conflict by raising a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exception.

For added clarity on the point above, consider this illustration:

```python
x = 1
def f():
    # The next line is a syntax error
    exec 'x=2'
    def g():
        return x

```

The `exec` statement on line 4 is a syntax error, because `exec` would introduce a fresh local variable called `x` whose value `g()` is meant to read.

Since `exec` shows up infrequently across most Python code (and where it does appear, it’s frequently a hint of weak design anyway), this restriction shouldn’t prove burdensome.

Out of compatibility caution, nested scopes arrive in stages; under Python 2.1 they stay off by default, though a module can switch them on with a future statement of the kind documented in [**PEP 236**](https://peps.python.org/pep-0236/). (The next section covers [**PEP 236**](https://peps.python.org/pep-0236/) in more depth.) Come Python 2.2, nested scopes turn into the default behavior with no option to disable them, but everyone will have had the whole span of 2.1’s life to repair anything their arrival breaks.

See also

[**PEP 227**](https://peps.python.org/pep-0227/) - Statically Nested Scopes

Written and implemented by Jeremy Hylton.

[Subject index](INDEX.md) · [Previous source section](introduction.md) · [Next source section](pep-236-future-directives.md) · [Release/subject declaration](introduction.md)
