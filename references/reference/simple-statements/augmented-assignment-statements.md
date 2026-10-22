# 7.2.1. Augmented assignment statements

### 7.2.1. Augmented assignment statements

Augmented assignment merges, inside one statement, a binary operation together with an assignment statement:

```text

augmented_assignment_stmt: augtarget augop (expression_list | yield_expression)
augtarget:                 identifier | attributeref | subscription
augop:                     "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
                           | ">>=" | "<<=" | "&=" | "^=" | "|="
```

(Consult the section [Primaries](https://docs.python.org/3.14/reference/expressions.html#primaries) for the grammar definitions of the final three symbols.)

An augmented assignment evaluates the target (which, in contrast to ordinary assignment statements, cannot be an unpacking) along with the expression list, applies the binary operation tied to the kind of assignment to the two operands, and binds the result to the original target. The target is evaluated only one time.

An augmented assignment statement such as `x += 1` may be restated as `x = x + 1` to reach a comparable, though not identical, outcome. Within the augmented form, `x` is evaluated only one time. Furthermore, where feasible, the operation itself is carried out *in-place*, which means that instead of building a new object and binding it to the target, the existing object is modified in place.

In contrast to ordinary assignments, augmented assignments evaluate the left-hand side *before* they evaluate the right-hand side. To illustrate, `a[i] += f(x)` first looks up `a[i]`, then evaluates `f(x)` and carries out the addition, and finally writes the result back into `a[i]`.

Apart from assigning to tuples and to multiple targets in one statement, the assignment that augmented assignment statements perform proceeds in the same fashion as ordinary assignments. In the same way, apart from the potential *in-place* behavior, the binary operation that augmented assignment performs matches the ordinary binary operations.

When targets are attribute references, the same caution regarding class and instance attributes holds as it does for regular assignments.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Owning language section](assignment-statements.md) · [Previous source section](assignment-statements.md) · [Following source section](annotated-assignment-statements.md)
