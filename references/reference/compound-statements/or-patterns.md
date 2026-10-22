# 8.6.4.1. OR Patterns

#### 8.6.4.1. OR Patterns

Two or more patterns joined by vertical bars `|` form an OR pattern. Syntax:

```text

or_pattern: "|".closed_pattern+
```

Irrefutability is allowed only on the last subpattern, and every subpattern has to bind an identical set of names so that no ambiguity arises.

The subject value is matched against each subpattern of an OR pattern one by one, stopping at the first that passes; the OR pattern then counts as successful. If, however, every subpattern fails, then so does the OR pattern.

Put simply, `P1 | P2 | ...` first tries `P1`; on failure it moves to `P2`, and so on, returning success the moment any one matches and failing if none do.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](patterns.md) · [Following source section](as-patterns.md)
