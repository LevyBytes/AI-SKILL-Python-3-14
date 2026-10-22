# 4.9.8. Function Annotations

### 4.9.8. Function Annotations

[Function annotations](https://docs.python.org/3.14/reference/compound_stmts.html#function) are entirely optional metadata describing the types that user-defined functions work with (consult [**PEP 3107**](https://peps.python.org/pep-3107/) and [**PEP 484**](https://peps.python.org/pep-0484/) for further detail).

A function keeps its [Annotations](https://docs.python.org/3.14/glossary.html#term-function-annotation) inside the [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attribute as a dictionary, and they influence no other aspect of the function. You write a parameter annotation as a colon after the parameter's name, trailed by an expression whose value becomes the annotation. A return annotation takes the form of a literal `->` plus an expression, positioned between the parameter list and the colon that closes the [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def) statement. The sample beneath annotates a mandatory argument, an optional one, and the return value:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'

```

[Subject index](INDEX.md) · [Previous source section](documentation-strings.md) · [Following source section](intermezzo-coding-style.md)
