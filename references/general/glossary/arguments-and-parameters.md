# Arguments and parameters

Open when checking Python definitions for arguments and parameters.

## argument

A value handed to a function (or method) at the moment you call it. Two varieties of argument exist:

- *keyword argument*: an argument introduced by an identifier (e.g. `name=`) within a function call, or supplied as a value inside a dictionary prefixed with `**`. To illustrate, `3` and `5` each act as keyword arguments in these calls to [`complex()`](https://docs.python.org/3.14/library/functions.html#complex):

```python
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})

```

- *positional argument*: any argument that is not a keyword argument. Such arguments may sit at the start of an argument list and/or be supplied as members of an iterable prefixed with `*`. As an example, `3` and `5` are each positional arguments in these calls:

```python
complex(3, 5)
complex(*(3, 5))

```

Inside a function body, arguments get bound to the named local variables. The [Calls](https://docs.python.org/3.14/reference/expressions.html#calls) section spells out the rules that drive this binding. From a syntax standpoint, an argument may be written as any expression; its computed value is then bound to the local variable.

Refer as well to the parameter glossary entry, the FAQ item covering [the difference between arguments and parameters](https://docs.python.org/3.14/faq/programming.html#faq-argument-vs-parameter), and [**PEP 362**](https://peps.python.org/pep-0362/).

## positional argument

See argument.

## keyword argument

See argument.

## parameter

A named entity inside a function (or method) definition that designates an argument (or, in some instances, arguments) the function is able to take. Parameters come in five kinds:

- *positional-or-keyword*: designates an argument that may be passed either by position or as a keyword argument. This is the parameter's default kind, for instance *foo* and *bar* below:

```python
def func(foo, bar=None): ...

```

- *positional-only*: designates an argument supplied solely by position. You define positional-only parameters by placing a `/` character into the function definition's parameter list after them, for instance *posonly1* and *posonly2* below:

```python
def func(posonly1, posonly2, /, positional_or_keyword): ...

```

- *keyword-only*: designates an argument supplied solely by keyword. You define keyword-only parameters by placing a single var-positional parameter or a bare `*` into the function definition's parameter list ahead of them, for instance *kw_only1* and *kw_only2* below:

```python
def func(arg, *, kw_only1, kw_only2): ...

```

- *var-positional*: designates that an arbitrary sequence of positional arguments may be given (over and above any positional arguments other parameters already take). You define such a parameter by putting `*` ahead of the parameter name, for instance *args* below:

```python
def func(*args, **kwargs): ...

```

- *var-keyword*: designates that arbitrarily many keyword arguments may be given (over and above any keyword arguments other parameters already take). You define such a parameter by putting `**` ahead of the parameter name, for instance *kwargs* in the example just above.

Parameters can designate both optional and required arguments, and can supply default values for certain optional arguments.

For more, consult the argument glossary entry, the FAQ item covering [the difference between arguments and parameters](https://docs.python.org/3.14/faq/programming.html#faq-argument-vs-parameter), the [`inspect.Parameter`](https://docs.python.org/3.14/library/inspect.html#inspect.Parameter) class, the [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) section, plus [**PEP 362**](https://peps.python.org/pep-0362/).

[Glossary context index](INDEX.md).
