# 5.7. More on Conditions

### 5.7. More on Conditions

Whatever conditions sit inside `while` and `if` statements may hold any operators, not comparisons alone.

The `in` and `not in` comparison operators are membership tests checking whether some value does (or does not) appear inside a container. The `is` and `is not` operators check whether a pair of objects are genuinely the very same object. Every comparison operator shares one priority, and that priority sits below every numerical operator.

Chaining comparisons is allowed. To take one case, `a < b == c` checks whether `a` falls below `b` and on top of that whether `b` equals `c`.

Comparisons can be linked using the Boolean operators `and` and `or`, while the result of a comparison (or of any other Boolean expression) admits negation through `not`. These rank below the comparison operators in priority; among themselves, `not` ranks highest and `or` ranks lowest, making `A and not B or C` equivalent to `(A and (not B)) or C`. Parentheses, as ever, let you spell out whatever grouping you intend.

The Boolean operators `and` and `or` count as so-called *short-circuit* operators: their arguments get evaluated left to right, and the evaluation halts the moment the result is settled. To illustrate, when `A` and `C` hold true while `B` is false, `A and B and C` never evaluates the expression `C`. Used as a plain value instead of as a Boolean, a short-circuit operator returns whichever argument it evaluated last.

You may also store the result of a comparison or another Boolean expression into a variable. As an example,

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'

```

Note that Python, in contrast to C, makes you spell out assignment inside an expression with the [walrus operator](https://docs.python.org/3.14/faq/design.html#why-can-t-i-use-an-assignment-in-an-expression) `:=`. Doing so heads off a familiar category of bugs in C programs: writing `=` within an expression when you meant `==`.

[Subject index](INDEX.md) · [Previous source section](sorted-unique-iteration-and-filtered-copies.md) · [Following source section](comparing-sequences-and-other-types.md)
