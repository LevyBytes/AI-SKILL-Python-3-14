# 8.6.4.9. Mapping Patterns

#### 8.6.4.9. Mapping Patterns

A mapping pattern holds one or more key-value patterns. Its syntax resembles building a dictionary. Syntax:

```text

mapping_pattern:     "{" [items_pattern] "}"
items_pattern:       ",".key_value_pattern+ ","?
key_value_pattern:   (literal_pattern | value_pattern) ":" pattern
                     | double_star_pattern
double_star_pattern: "**" capture_pattern
```

A mapping pattern may include no more than one double star pattern, and that double star pattern has to be its final subpattern.

Mapping patterns may not contain duplicate keys. Duplicate literal keys cause a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). Two distinct keys that nonetheless share a value cause a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) at runtime.

Matching a mapping pattern against a subject value proceeds logically as follows:

1.

When the subject value is not a mapping [3], the mapping pattern fails.

2.

When each key listed in the mapping pattern is found in the subject mapping, and each such key's pattern matches that key's corresponding item in the subject mapping, the mapping pattern passes.

3.

When duplicate keys turn up in the mapping pattern, that pattern is treated as invalid. Duplicate literal values trigger a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError); named keys sharing a value trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Note

The two-argument form of the subject mapping's `get()` method is used to match key-value pairs. A matched key-value pair has to already exist in the mapping rather than being generated on the fly through [`__missing__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__missing__) or [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__).

Put simply, `{KEY1: P1, KEY2: P2, ... }` matches only when all of the following hold:

- check `<subject>` is a mapping

- `KEY1 in <subject>`

- `P1` matches `<subject>[KEY1]`

- ? and so on across each corresponding KEY/pattern pair.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](sequence-patterns.md) · [Following source section](class-pattern-matching.md)
