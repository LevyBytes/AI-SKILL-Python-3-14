# 6.3.3. Calls

### 6.3.3. Calls

A call invokes a callable object (for instance, a [function](https://docs.python.org/3.14/glossary.html#term-function)) using a series of [arguments](https://docs.python.org/3.14/glossary.html#term-argument) that may be empty:

```text

call:                 primary "(" [argument_list [","] | comprehension] ")"
argument_list:        positional_arguments ["," starred_and_keywords]
                        ["," keywords_arguments]
                      | starred_and_keywords ["," keywords_arguments]
                      | keywords_arguments
positional_arguments: positional_item ("," positional_item)*
positional_item:      assignment_expression | "*" expression
starred_and_keywords: ("*" expression | keyword_item)
                      ("," "*" expression | "," keyword_item)*
keywords_arguments:   (keyword_item | "**" expression)
                      ("," keyword_item | "," "**" expression)*
keyword_item:         identifier "=" expression
```

You may include an optional trailing comma following the positional and keyword arguments, though it has no effect on the semantics.

The primary is required to yield a callable object — the callables comprise user-defined functions, built-in functions, methods belonging to built-in objects, class objects, methods belonging to class instances, plus every object furnished with a [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method. Every argument expression gets evaluated before the call itself is attempted. For the syntax of formal [parameter](https://docs.python.org/3.14/glossary.html#term-parameter) lists, see section [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function).

When keyword arguments appear, they get translated into positional arguments first, in this way. To begin, a list of empty slots is set up for the formal parameters. Given N positional arguments, those go into the first N slots. After that, every keyword argument has its identifier used to find the matching slot (when the identifier equals the first formal parameter name, the first slot applies, and so forth). Should the slot already hold a value, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised. Failing that, the argument goes into the slot and fills it (the slot is filled even if the expression happens to be `None`). After every argument has been handled, any slots that remain empty get populated with the matching default value taken from the function definition. (Default values get computed a single time, at the moment the function is defined; consequently, a mutable object — say a list or a dictionary — used as a default value ends up shared across every call that omits an argument value for that slot; you should normally steer clear of this.) Should any empty slots remain that have no default value specified, a `TypeError` exception is raised. Failing that, the list of filled slots serves as the argument list for the call.

**CPython implementation detail:** An implementation is allowed to offer built-in functions whose positional parameters have no names, even when they are ‘named’ for the sake of documentation, and which for that reason cannot be passed by keyword. Within CPython, this applies to functions written in C that rely on [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) to parse their arguments.

Should the supplied positional arguments outnumber the available formal parameter slots, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised, except where a formal parameter written with the syntax `*identifier` exists; under that condition, that formal parameter is handed a tuple holding the surplus positional arguments (or an empty tuple when there was no surplus positional argument).

When any keyword argument fails to match a formal parameter name, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised, except where a formal parameter written with the syntax `**identifier` exists; under that condition, that formal parameter is handed a dictionary holding the surplus keyword arguments (with the keywords as keys and the argument values as the matching values), or else a (new) empty dictionary when there was no surplus keyword argument.

Should the syntax `*expression` show up within the function call, `expression` has to evaluate to an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable). The elements drawn from these iterables are handled as though they were extra positional arguments. Take the call `f(x1, x2, *y, x3, x4)`: should *y* evaluate to a sequence *y1*, …, *yM*, this matches a call carrying M+4 positional arguments *x1*, *x2*, *y1*, …, *yM*, *x3*, *x4*.

One result of this is that even though the `*expression` syntax can show up *after* explicit keyword arguments, it gets processed *before* the keyword arguments (along with any `**expression` arguments – see below). Thus:

```python
>>> def f(a, b):
...     print(a, b)
...
>>> f(b=1, *(2,))
2 1
>>> f(a=1, *(2,))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got multiple values for keyword argument 'a'
>>> f(1, *(2,))
1 2

```

Having both keyword arguments and the `*expression` syntax within one call is uncommon, so this confusion seldom comes up in real code.

Should the syntax `**expression` show up within the function call, `expression` has to evaluate to a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping), whose contents are handled as extra keyword arguments. Should a parameter that matches a key already hold a value (whether from an explicit keyword argument or from a separate unpacking), a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised.

Whenever `**expression` is in play, every key within that mapping has to be a string. Each value taken from the mapping is bound to the first formal parameter that is eligible for keyword assignment and whose name equals the key. The key is not required to be a Python identifier (for instance, `"max-temp °F"` is allowed, though it will fail to match any declarable formal parameter). When no formal parameter matches, the key-value pair gets gathered by the `**` parameter if one exists, and otherwise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised.

Formal parameters written with the syntax `*identifier` or `**identifier` may not serve as positional argument slots, nor as keyword argument names.

Changed in version 3.5: Function calls allow any quantity of `*` and `**` unpackings, positional arguments are permitted after iterable unpackings (`*`), and keyword arguments are permitted after dictionary unpackings (`**`). This was first proposed by [**PEP 448**](https://peps.python.org/pep-0448/).

A call always hands back some value, possibly `None`, except when it raises an exception. The way that value gets computed hinges on the type of the callable object.

If it is—

a user-defined function:

The code block belonging to the function runs, receiving the argument list. The first action that code block performs is binding the formal parameters to the arguments; section [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) covers this. Whenever the code block runs a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement, that fixes the return value of the function call. Should execution arrive at the end of the code block without any `return` statement having run, the return value is `None`.

a built-in function or method:

The outcome rests with the interpreter; consult [Built-in Functions](https://docs.python.org/3.14/library/functions.html#built-in-funcs) for the descriptions of the built-in functions and methods.

a class object:

A fresh instance of that class is handed back.

a class instance method:

The matching user-defined function gets called, given an argument list one item longer than the call's argument list: the instance takes the first argument position.

a class instance:

The class is required to define a [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method; the result is then identical to calling that method.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [Previous source section](formal-subscription-grammar.md) · [Following source section](await-expression.md)
