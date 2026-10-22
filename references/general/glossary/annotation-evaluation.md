# Annotation evaluation

Open when checking Python definitions for annotation evaluation.

## annotation

A label tied to a variable, a class attribute, or a function's parameter or return value, conventionally serving as a type hint.

While annotations on local variables are unavailable at runtime, those on global variables, class attributes, and functions can be obtained by invoking [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) against modules, classes, and functions, respectively.

Consult variable annotation, function annotation, and [**PEP 484**](https://peps.python.org/pep-0484/), [**PEP 526**](https://peps.python.org/pep-0526/), and [**PEP 649**](https://peps.python.org/pep-0649/), which lay out this functionality. The [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto) guide also covers recommended ways to handle annotations.

## annotate function

A callable you can invoke to fetch an object's annotations. Such functions are typically plain functions, generated automatically as the [`__annotate__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotate__) attribute on functions, classes, and modules. Annotate functions form a subset of evaluate functions.

## evaluate function

A function invocable to compute a lazily evaluated attribute belonging to an object, for instance the value of type aliases produced by the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement.

## function annotation

An annotation applied to a function's return value or to a function parameter.

Type hints are the usual purpose of function annotations: for instance, the function below is meant to accept two [`int`](https://docs.python.org/3.14/library/functions.html#int) arguments and likewise to return an `int`:

```python
def sum_two_numbers(a: int, b: int) -> int:
   return a + b

```

The [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) section covers function annotation syntax.

See variable annotation along with [**PEP 484**](https://peps.python.org/pep-0484/), where this capability is described. Refer as well to [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto) for guidance on handling annotations.

## variable annotation

An annotation attached to a variable or a class attribute.

In annotating a variable or a class attribute, the assignment is optional:

```python
class C:
    field: 'annotation'

```

Variable annotations typically serve type hints: for instance this variable is expected to hold [`int`](https://docs.python.org/3.14/library/functions.html#int) values:

```python
count: int = 0

```

The syntax of variable annotation is spelled out in the section [Annotated assignment statements](https://docs.python.org/3.14/reference/simple_stmts.html#annassign).

Consult function annotation along with [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 526**](https://peps.python.org/pep-0526/), where this functionality is laid out. For recommended ways to handle annotations, look as well at [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto).

[Glossary context index](INDEX.md).
