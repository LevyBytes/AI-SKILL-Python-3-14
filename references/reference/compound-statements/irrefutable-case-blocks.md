# 8.6.3. Irrefutable Case Blocks

### 8.6.3. Irrefutable Case Blocks

A match-all case block is what we call an irrefutable case block. Within a single match statement there can be no more than one such block, and where present it has to come last.

We treat a case block as irrefutable when it carries no guard and its pattern itself is irrefutable. A pattern counts as irrefutable when its syntax alone is enough to guarantee it always passes. The irrefutable patterns are limited to these:

- AS Patterns whose left-hand side is irrefutable

- OR Patterns containing at least one irrefutable pattern

- Capture Patterns

- Wildcard Patterns

- parenthesized irrefutable patterns

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Previous source section](guards.md) · [Following source section](patterns.md)
