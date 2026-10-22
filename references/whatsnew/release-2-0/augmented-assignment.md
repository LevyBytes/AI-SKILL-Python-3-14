# What’s New in Python 2.0 / Augmented Assignment

### Augmented Assignment

Augmented assignment operators, yet another long-sought feature, have arrived in Python 2.0. Augmented assignment operators take in `+=`, `-=`, `*=`, and the like. For instance, the statement `a += 2` raises the value of the variable `a` by 2, matching the marginally wordier `a = a + 2`.

The complete roster of supported assignment operators is `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `&=`, `|=`, `^=`, `>>=`, and `<<=`. Python classes are able to override the augmented assignment operators by supplying methods called `__iadd__()`, `__isub__()`, and so on. To illustrate, the `Number` class below keeps a number and supports applying += to produce a new instance whose value has been incremented.

```python
class Number:
    def __init__(self, value):
        self.value = value
    def __iadd__(self, increment):
        return Number( self.value + increment)

n = Number(5)
n += 3
print n.value

```

The `__iadd__()` special method receives the increment’s value and is expected to return a new instance carrying a suitably altered value; that return value becomes the new value bound to the variable on the left-hand side.

Augmented assignment operators originally appeared in the C programming language, and the majority of C-derived languages, including **awk**, C++, Java, Perl, and PHP, support them as well. The augmented assignment patch was the work of Thomas Wouters.

[Subject index](INDEX.md) · [Previous source section](list-comprehensions.md) · [Next source section](string-methods.md) · [Release/subject declaration](introduction.md)
