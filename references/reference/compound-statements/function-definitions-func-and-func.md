# compound statements: Function definitions, binding and decorators

### 8.7. Function definitions

A user-defined function object is defined by a function definition (refer to the [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types) section):

```text

funcdef:                   [decorators] "def" funcname [type_params] "(" [parameter_list] ")"
                           ["->" expression] ":" suite
decorators:                decorator+
decorator:                 "@" assignment_expression NEWLINE
parameter_list:            defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
                             | parameter_list_no_posonly
parameter_list_no_posonly: defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                           | parameter_list_starargs
parameter_list_starargs:   "*" star_parameter ("," defparameter)* ["," [parameter_star_kwargs]]
                           | "*" ("," defparameter)+ ["," [parameter_star_kwargs]]
                           | parameter_star_kwargs
parameter_star_kwargs:     "**" parameter [","]
parameter:                 identifier [":" expression]
star_parameter:            identifier [":" ["*"] expression]
defparameter:              parameter ["=" expression]
funcname:                  identifier
```

An executable statement is what a function definition is. Running it binds the function name within the current local namespace to a function object (which wraps the function's executable code). Held inside that function object is a reference to the present global namespace, which serves as the global namespace in effect when the function gets called.

Running a function definition does not run the function body; the body runs only at call time. [4]

One or more [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) expressions may surround a function definition. These decorator expressions are evaluated at definition time, within the scope enclosing the function definition. Each must yield a callable, which then receives the function object as its sole argument. What that call returns is bound to the function name in place of the function object. When several decorators are present, they nest. As an illustration, this code

```python
@f1(arg)
@f2
def func(): pass

```

is roughly equivalent to

```python
def func(): pass
func = f1(arg)(f2(func))

```

except that the original function is not temporarily bound to the name `func`.

Changed in version 3.9: Any valid [`assignment_expression`](https://docs.python.org/3.14/reference/expressions.html#grammar-token-python-grammar-assignment_expression) is now permitted as a decorator on functions. The grammar used to be far stricter; refer to [**PEP 614**](https://peps.python.org/pep-0614/) for the specifics.

Between the function's name and the opening parenthesis of its parameter list, type parameters may be supplied within square brackets. This signals to static type checkers that the function is generic. While running, those type parameters are reachable through the function's [`__type_params__`](https://docs.python.org/3.14/reference/datamodel.html#function.__type_params__) attribute. See Generic functions for more.

Changed in version 3.12: Lists of type parameters first arrived in Python 3.12.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Following source contract continuation](function-definitions-whats-on-the-telly.md) · [Previous source section](class-patterns-2.md)
