# 8.6.4.8. Sequence Patterns

#### 8.6.4.8. Sequence Patterns

Several subpatterns are held within a sequence pattern, each to be matched against the elements of a sequence. Its syntax resembles unpacking a list or a tuple.

```text

sequence_pattern:       "[" [maybe_sequence_pattern] "]"
                        | "(" [open_sequence_pattern] ")"
open_sequence_pattern:  maybe_star_pattern "," [maybe_sequence_pattern]
maybe_sequence_pattern: ",".maybe_star_pattern+ ","?
maybe_star_pattern:     star_pattern | pattern
star_pattern:           "*" (capture_pattern | wildcard_pattern)
```

Whether you write a sequence pattern with parentheses or square brackets makes no difference (i.e. `(...)` vs `[...]` ).

Note

When a single pattern is wrapped in parentheses and lacks a trailing comma (e.g. `(3 | 4)`), it is a group pattern. A single pattern inside square brackets (e.g. `[3 | 4]`), on the other hand, remains a sequence pattern.

A sequence pattern may hold at most one star subpattern, and that star subpattern can appear anywhere within it. Lacking a star subpattern makes the sequence pattern fixed-length; having one makes it variable-length.

Matching a sequence pattern against a subject value proceeds logically as follows:

1.

When the subject value is not a sequence [2], the sequence pattern fails.

2.

When the subject value is a `str`, `bytes` or `bytearray` instance, the sequence pattern fails.

3.

What happens next hinges on whether the sequence pattern is fixed- or variable-length.

When the sequence pattern is fixed-length:

  1.

When the subject sequence's length differs from the count of subpatterns, the sequence pattern fails

  2.

The sequence pattern's subpatterns are matched left to right against the matching items of the subject sequence. The first subpattern to fail halts matching. The sequence pattern passes when every subpattern matches its corresponding item.

When the sequence pattern is instead variable-length:

  1.

When the subject sequence's length falls below the count of non-star subpatterns, the sequence pattern fails.

  2.

As with fixed-length sequences, the leading non-star subpatterns are matched to their corresponding items.

  3.

When that step passes, the star subpattern captures a list built from the leftover subject items, leaving out those leftover items that line up with non-star subpatterns appearing after the star subpattern.

  4.

The remaining non-star subpatterns are then matched to their corresponding subject items, just as in a fixed-length sequence.

Note

A subject sequence's length comes from [`len()`](https://docs.python.org/3.14/library/functions.html#len) (that is, through the [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) protocol). The interpreter may cache this length much as it does for value patterns.

Put simply, `[P1, P2, P3,` ? `, P<N>]` matches only when all of the following hold:

- check `<subject>` is a sequence

- `len(subject) == <N>`

- `P1` matches `<subject>[0]` (note that this match can also bind names)

- `P2` matches `<subject>[1]` (note that this match can also bind names)

- ? and so on across each corresponding pattern/element.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](group-patterns.md) · [Following source section](mapping-patterns.md)
