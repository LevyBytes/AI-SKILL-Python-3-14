# 6.15. Expression lists

### 6.15. Expression lists

```text

starred_expression:       "*" or_expr | expression
flexible_expression:      assignment_expression | starred_expression
flexible_expression_list: flexible_expression ("," flexible_expression)* [","]
starred_expression_list:  starred_expression ("," starred_expression)* [","]
expression_list:          expression ("," expression)* [","]
yield_list:               expression_list | starred_expression "," [starred_expression_list]
```

Save for when it forms part of a list or set display, an expression list that holds at least one comma produces a tuple. That tuple's length equals how many expressions the list contains. Evaluation of the expressions runs left to right.

The asterisk `*` marks *iterable unpacking*. Whatever it operates on has to be an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable). That iterable gets spread out into a run of items, which land in the new tuple, list, or set right where the unpacking sits.

Added in version 3.5: Iterable unpacking within expression lists, first put forward by [**PEP 448**](https://peps.python.org/pep-0448/).

Added in version 3.11: Every item of an expression list is allowed to be starred. Consult [**PEP 646**](https://peps.python.org/pep-0646/).

You only need a trailing comma to form a one-item tuple, like `1,`; in all other situations it is optional. One expression lacking a trailing comma makes no tuple but rather returns that expression's value. (For an empty tuple, write an empty pair of parentheses: `()`.)

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](lambdas.md) · [Following source section](evaluation-order.md)
