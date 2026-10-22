# compound statements: Default parameters and argument binding

A function is said to have “default parameter values” whenever one or more of its [parameters](https://docs.python.org/3.14/glossary.html#term-parameter) take the form *parameter* `=` *expression*. Where a parameter carries a default, a call may leave out the matching [argument](https://docs.python.org/3.14/glossary.html#term-argument); the parameter then takes on its default instead. Once any parameter is given a default, every parameter that follows it up to the “`*`” is also required to carry one — a syntactic rule the grammar itself does not capture.

**When the function definition runs, its default parameter values are computed in left-to-right order.** Consequently, each such expression runs a single time — at the moment the function is defined — and that same “pre-computed” result is reused on every subsequent call. The point matters most when the default happens to be a mutable object, like a list or a dictionary: should the function alter that object (for instance, by appending to a list), the default parameter value itself ends up altered. That outcome is rarely the desired one. The customary workaround is to default to `None` and check for it explicitly inside the function body, like so:

```python
def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin

```

Section [Calls](https://docs.python.org/3.14/reference/expressions.html#calls) covers function call semantics at greater length. Every function call gives a value to all of the parameters named in the parameter list, drawing it from positional arguments, from keyword arguments, or from defaults. When the form “`*identifier`” appears, it gets set up as a tuple collecting any leftover positional parameters and defaults to the empty tuple. When the form “`**identifier`” appears, it gets set up as a fresh ordered mapping collecting any leftover keyword arguments and defaults to a new empty mapping of that same type. Anything after “`*`” or “`*identifier`” becomes a keyword-only parameter, passable solely via keyword arguments. Anything before “`/`” becomes a positional-only parameter, passable solely via positional arguments.

Changed in version 3.8: Positional-only parameters can be marked with the `/` function parameter syntax. Refer to [**PEP 570**](https://peps.python.org/pep-0570/) for the specifics.

A parameter may carry an [annotation](https://docs.python.org/3.14/glossary.html#term-function-annotation) written as “`: expression`” after the parameter name. This applies to any parameter, including ones written `*identifier` or `**identifier`. (One special case: a parameter of the form `*identifier` may carry an annotation written “`: *expression`”.) A function may additionally take a “return” annotation written “`-> expression`” after the parameter list. Such annotations may be any valid Python expression, and their presence leaves a function’s semantics unchanged. Consult Annotations for further detail on annotations.

Changed in version 3.11: An annotation written “`: *expression`” is now permitted on parameters of the form “`*identifier`”. See [**PEP 646**](https://peps.python.org/pep-0646/).

Anonymous functions — ones never bound to a name — can also be built for direct use within expressions. These rely on lambda expressions, covered in section [Lambdas](https://docs.python.org/3.14/reference/expressions.html#lambda). Keep in mind that a lambda expression is only shorthand for a stripped-down function definition; a function written via a “`def`” statement can be handed around or assigned to a different name exactly as one written via a lambda can. In fact the “`def`” form carries more power, since it permits both multiple statements and annotations.

**Programmer’s note:** Functions are first-class objects. Running a “`def`” statement within a function definition creates a local function that may be handed back or passed around. Free variables referenced by the nested function can reach the local variables of the enclosing function that holds the def. Section [Naming and binding](https://docs.python.org/3.14/reference/executionmodel.html#naming) has the details.

See also

[**PEP 3107**](https://peps.python.org/pep-3107/) - Function Annotations

The first specification that defined function annotations.

[**PEP 484**](https://peps.python.org/pep-0484/) - Type Hints

Establishes a standard interpretation of annotations as type hints.

[**PEP 526**](https://peps.python.org/pep-0526/) - Syntax for Variable Annotations

Lets variable declarations carry type hints, covering class variables and instance variables alike.

[**PEP 563**](https://peps.python.org/pep-0563/) - Postponed Evaluation of Annotations

Enables forward references inside annotations by keeping them as strings at runtime rather than evaluating them eagerly.

[**PEP 318**](https://peps.python.org/pep-0318/) - Decorators for Functions and Methods

Added decorators for functions and methods. Decorators for classes arrived later in [**PEP 3129**](https://peps.python.org/pep-3129/).

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](function-definitions-func-and-func.md) · [Previous source contract continuation](function-definitions-func-and-func.md) · [Following source section](class-definitions.md)
