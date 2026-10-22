# 6.3.2.4. Formal subscription grammar

#### 6.3.2.4. Formal subscription grammar

```text

subscription:     primary '[' subscript ']'
subscript:        single_subscript | tuple_subscript
single_subscript: proper_slice | assignment_expression
proper_slice:     [expression] ":" [expression] [ ":" [expression] ]
tuple_subscript:  ','.(single_subscript | starred_expression)+ [',']
```

Bear in mind that the `|` operator [denotes ordered choice](https://docs.python.org/3.14/reference/introduction.html#notation). Concretely, within `subscript`, when both alternatives are capable of matching, priority goes to the first one (`single_subscript`).

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [Owning language section](subscriptions-and-slicings.md) · [Previous source section](starred-subscriptions.md) · [Following source section](calls.md)
