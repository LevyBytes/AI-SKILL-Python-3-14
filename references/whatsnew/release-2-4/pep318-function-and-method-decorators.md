# Python 2.4 changes: Parameterized decorators and type-checking examples

```python
def require_int (func):
    def wrapper (arg):
        assert isinstance(arg, int)
        return func(arg)

    return wrapper

@require_int
def p1 (arg):
    print arg

@require_int
def p2(arg):
    print arg*2

```

[**PEP 318**](https://peps.python.org/pep-0318/) includes a sample with a more elaborate take on this concept, one that lets you name the required type and also verify the type that comes back.

Decorator functions are allowed to accept arguments. When arguments get passed, your decorator function is invoked with just those arguments and has to return a brand-new decorator function; that function then has to accept a single function and return a function, exactly as outlined above. Put differently, `@A @B @C(args)` turns into:

```python
def f(): ...
_deco = C(args)
f = A(B(_deco(f)))

```

Wrapping your head around this can twist your brain a little, though it isn’t especially hard.

A minor companion change makes a function’s [`func_name`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__) attribute writable. Because that attribute drives how function names show up in tracebacks, a decorator ought to update the name on whatever new function it builds and returns.

See also

[**PEP 318**](https://peps.python.org/pep-0318/) - Decorators for Functions, Methods and Classes

Authored by Kevin D. Smith, Jim Jewett, and Skip Montanaro. A number of people contributed patches that implemented function decorators, but the patch that actually got committed was #979728, authored by Mark Russell.

[https://wiki.python.org/moin/PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)

You’ll find several decorator examples on this Wiki page.

[Subject index](INDEX.md) · [Previous source section](function-method-decorators.md) · [Next source section](pep-322-reverse-iteration.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Release/subject declaration](function-method-decorators.md)
