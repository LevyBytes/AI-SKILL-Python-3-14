# Why does -22 // 10 return -3?

### Why does -22 // 10 return -3?

The main motivation is wanting `i % j` to carry the same sign as `j`. Given that goal, plus the desire that:

```python
i == (i // j) * j + (i % j)

```

it follows that integer division must round toward the floor. C imposes that identity too, so compilers there that truncate `i // j` must arrange for `i % j` to share the sign of `i`.

Genuine use cases for `i % j` with a negative `j` are scarce. With a positive `j`, however, they abound, and nearly all of them benefit from `i % j` being `>= 0`. If the clock currently reads 10, what did it read 200 hours earlier? `-190 % 12 == 2` is handy; `-190 % 12 == -10` is a bug lying in wait to strike.

[Subject index](INDEX.md)
