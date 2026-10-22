# Names and scopes

Open when checking Python definitions for names and scopes.

## namespace

The location at which a variable lives. Dictionaries are how namespaces get implemented. Alongside the local, global and built-in namespaces there exist nested namespaces inside objects (within methods). By heading off naming clashes, namespaces enable modularity. As a case in point, the functions [`builtins.open`](https://docs.python.org/3.14/library/functions.html#open) and [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) are told apart through their namespaces. Namespaces also help readability and maintainability by signaling which module supplies a given function. To illustrate, putting [`random.seed()`](https://docs.python.org/3.14/library/random.html#random.seed) or [`itertools.islice()`](https://docs.python.org/3.14/library/itertools.html#itertools.islice) signals plainly that the [`random`](https://docs.python.org/3.14/library/random.html#module-random) and [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) modules respectively supply those functions.

## nested scope

The capacity to reference a variable held in an enclosing definition. As an example, a function declared inside another function can reference variables belonging to the outer function. Be aware that by default nested scopes apply to reference only and not to assignment. Local variables get both read and written within the innermost scope. In the same way, global variables are read from and written to the global namespace. Writing to outer scopes is enabled by [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal).

## free variable

In the strict sense, per the [language execution model](https://docs.python.org/3.14/reference/executionmodel.html#bind-names), a free variable denotes any variable referenced within a namespace that is not local to that namespace. Consult closure variable for an illustration. Pragmatically, owing to the naming of the [`codeobject.co_freevars`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_freevars) attribute, people occasionally treat the term as interchangeable with closure variable.

## closure variable

A free variable that a nested scope references and that an enclosing scope defines, instead of being looked up at runtime out of the globals or builtin namespaces. It may be stated explicitly with the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) keyword to grant write access, or stated implicitly when the variable is merely read.

To illustrate, inside the `inner` function in the code below, `x` and `print` are each free variables, yet `x` alone is a *closure variable*:

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print(x)
    return inner

```

Because the [`codeobject.co_freevars`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_freevars) attribute (which, its name notwithstanding, lists only the names of closure variables rather than every referenced free variable) exists, the broader free variable term occasionally gets used even where the real intent is to point specifically at closure variables.

## qualified name

A dotted name that traces the “path” from a module's global scope down to a class, function or method defined there, as laid out in [**PEP 3155**](https://peps.python.org/pep-3155/). With top-level functions and classes, the qualified name matches the object's name:

```python
>>> class C:
...     class D:
...         def meth(self):
...             pass
...
>>> C.__qualname__
'C'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'

```

Applied to modules, the *fully qualified name* refers to the complete dotted path leading to the module, parent packages included, e.g. `email.mime.text`:

```python
>>> import email.mime.text
>>> email.mime.text.__name__
'email.mime.text'

```

## optimized scope

A scope in which the compiler reliably knows the target local variable names at compile time, which permits optimizing read and write access to those names. Local namespaces of functions, generators, coroutines, comprehensions, and generator expressions are optimized this way. Note: the majority of interpreter optimizations reach every scope; only those depending on a fixed set of local and nonlocal variable names are confined to optimized scopes.

[Glossary context index](INDEX.md).
