# 8.6.2. Guards

### 8.6.2. Guards

```text

guard: "if" assignment_expression
```

A `guard`, attached to the `case`, has to pass before the body of the `case` block runs. Its shape is the keyword `if` trailed by an expression.

Here is how a `case` block carrying a `guard` proceeds logically:

1.

Verify that the pattern belonging to the `case` block matched. Should the pattern have failed, the `guard` goes unevaluated and the following `case` block is examined.

2.

Once the pattern has matched, the `guard` is evaluated.

  - Should the `guard` condition come out true, that case block becomes the chosen one.

  - Should the `guard` condition come out false, that case block is passed over.

  - Should the `guard` throw an exception while being evaluated, that exception propagates outward.

Since guards are expressions, they may carry side effects. Their evaluation runs through the case blocks in order, one after another, from first to last, bypassing any whose patterns fail to all match. (That is, guards must be evaluated in sequence.) As soon as one case block is chosen, guard evaluation halts.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Previous source section](overview.md) · [Following source section](irrefutable-case-blocks.md)
