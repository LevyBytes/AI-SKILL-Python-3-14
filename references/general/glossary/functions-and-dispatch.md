# Functions and dispatch

Open when checking Python definitions for functions and dispatch.

## function

A sequence of statements that hands some value back to a caller. Zero or more arguments may additionally be supplied to it, and those can figure in running the body. See also parameter, method, and the [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) section.

## callable

A callable is an object you can call, optionally supplying a collection of arguments (see argument), via the following syntax:

```python
callable(argument1, argument2, argumentN)

```

A function counts as a callable, and so by extension does a method. An instance of a class providing the [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method likewise counts as a callable.

## callback

A subroutine function handed in as an argument so that it can run at some later moment.

## lambda

A nameless inline function made up of one expression that gets evaluated at the moment the function is invoked. You write a lambda function with the syntax `lambda [parameters]: expression`

## decorator

A function that gives back another function, typically used as a function transformation through the `@wrapper` syntax. Familiar examples of decorators include [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) and [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod).

The decorator syntax is nothing more than syntactic sugar; the pair of function definitions below carry the same meaning:

```python
def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
    ...

```

That same idea applies to classes too, though it sees less use in that setting. For more on decorators, see the documentation for [function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) and [class definitions](https://docs.python.org/3.14/reference/compound_stmts.html#class).

## generic function

A function assembled from several functions, each realizing the same operation for a distinct type. The dispatch algorithm decides which implementation a particular call should employ.

See also the single dispatch glossary entry, the [`functools.singledispatch()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatch) decorator, and [**PEP 443**](https://peps.python.org/pep-0443/).

## single dispatch

A variety of generic function dispatch in which the implementation gets selected according to the type of one single argument.

[Glossary context index](INDEX.md).
