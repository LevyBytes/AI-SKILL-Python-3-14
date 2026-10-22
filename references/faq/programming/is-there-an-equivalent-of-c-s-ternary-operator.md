# Is there an equivalent of C’s “?:” ternary operator?

### Is there an equivalent of C’s “?:” ternary operator?

Yes, there is. Here is the syntax:

```python
[on_true] if [expression] else [on_false]

x, y = 50, 25
small = x if x < y else y

```

Prior to the arrival of this syntax in Python 2.5, a frequent idiom relied on logical operators:

```python
[expression] and [on_true] or [on_false]

```

That idiom, however, is unsafe, since it can produce incorrect results whenever *on_true* carries a false boolean value. For that reason, the `... if ... else ...` form is always the better choice.

[Subject index](INDEX.md)
