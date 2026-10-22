# 4.8. Defining Functions

### 4.8. Defining Functions

Let’s build a function that prints the Fibonacci series out to any chosen limit:

```python
>>> def fib(n):    # write Fibonacci series less than n
...     """Print a Fibonacci series less than n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

```

The keyword [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def) begins a function *definition*. After it come the function’s name and the parenthesized list of formal parameters. From the following line onward come the statements making up the function body, which have to be indented.

The opening statement of the body may, if you like, be a string literal; that string literal becomes the function’s documentation string, its *docstring*. (You’ll find more on docstrings in the Documentation Strings section.) Certain tools rely on docstrings to generate online or printed documentation automatically, or to let a user page through code interactively; weaving docstrings into the code you write is sound practice, so cultivate the habit.

*Executing* a function brings into being a fresh symbol table that holds its local variables. To be exact, every variable assignment inside a function records the value in the local symbol table; reading a variable, by contrast, consults the local symbol table first, then the local symbol tables of any enclosing functions, after that the global symbol table, and lastly the table of built-in names. Consequently you cannot assign directly to a global variable or to a variable of an enclosing function from inside a function (unless the global variable is named in a [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) statement, or the enclosing-function variable is named in a [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement), though you may still read them.

A call’s actual parameters (its arguments) get placed into the local symbol table of the function being invoked at the moment of the call; hence arguments use *call by value* (where that *value* is forever an object *reference*, never the object’s own value). [1] Whenever one function calls another, or invokes itself recursively, a brand-new local symbol table comes into existence for that call.

Defining a function binds its name to the function object within the current symbol table. The interpreter treats the object that name refers to as a user-defined function. Additional names may be made to refer to that very same function object and can serve to reach the function too:

```python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89

```

If your background is in other languages, you might protest that `fib` is a procedure rather than a function, on the grounds that it returns nothing. The truth is that even functions lacking a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement do hand back a value, albeit a fairly dull one. That value bears the name `None` (a built-in name). Ordinarily the interpreter won’t display the value `None` when it would be the sole thing written. If you genuinely wish to view it, use [`print()`](https://docs.python.org/3.14/library/functions.html#print):

```python
>>> fib(0)
>>> print(fib(0))
None

```

Writing a function that hands back a list of the Fibonacci numbers, rather than printing them, is straightforward:

```python
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

```

As is customary, this example brings several fresh Python features into view:

- The [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement exits a function and hands back a value. A `return` carrying no expression argument hands back `None`. Running off the end of a function likewise hands back `None`.

- The statement `result.append(a)` invokes a *method* on the list object `result`. By *method* we mean a function tied to a particular object, written as `obj.methodname`, where `obj` denotes some object (which may be an expression) and `methodname` names a method that the object’s type defines. Distinct types furnish distinct methods. Methods belonging to different types can share a name without any confusion arising. (Defining object types and methods of your own is possible by using *classes*; see [Classes](https://docs.python.org/3.14/tutorial/classes.html#tut-classes)) The method [`append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) demonstrated in the example is defined on list objects; it tacks a fresh element onto the list’s end. Here it amounts to the same thing as `result = result + [a]`, only more efficient.

[Subject index](INDEX.md) · [Previous source section](match-guards-mapping-patterns-captures-and-named-constants.md) · [Following source section](more-on-defining-functions.md)
