# 8.3. The `for` statement

### 8.3. The `for` statement

Iterating across the members of a sequence (a string, tuple or list, say) or another iterable object is done with the `for` statement:

```text

for_stmt: "for" target_list "in" starred_expression_list ":" suite
          ["else" ":" suite]
```

Evaluation of the [`starred_expression_list`](https://docs.python.org/3.14/reference/expressions.html#grammar-token-python-grammar-starred_expression_list) expression happens a single time; it ought to produce an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) object. From that iterable an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) is built. The iterator’s first item is then bound to the target list following the usual assignment rules (see [Assignment statements](https://docs.python.org/3.14/reference/simple_stmts.html#assignment)), and the suite runs. The same happens for every subsequent item the iterator hands out. Once the iterator runs dry, the suite in the `else` clause runs, if one exists, and the loop ends.

Running a [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) statement within the first suite ends the loop and skips the `else` clause’s suite entirely. Running a [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement within the first suite drops the remainder of the suite and moves on to the following item, or to the `else` clause when no further item remains.

Within the `for` loop, the variables in the target list get assigned. Doing so replaces every earlier assignment to those variables, including any performed inside the body of the `for` loop:

```python
for i in range(10):
    print(i)
    i = 5             # this will not affect the for-loop
                      # because i will be overwritten with the next
                      # index in the range

```

Once the loop ends, the names in the target list are not removed, yet should the sequence have been empty, the loop will never have assigned to them at all. Hint: the built-in type [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) stands for immutable arithmetic sequences of integers. As an example, stepping through `range(3)` produces 0, 1, and then 2 in turn.

Changed in version 3.11: The expression list may now include starred elements.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](the-while-statement.md) · [Following source section](the-try-statement.md)
