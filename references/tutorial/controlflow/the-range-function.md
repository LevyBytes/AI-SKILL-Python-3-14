# 4.3. The `range()` Function

### 4.3. The [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) Function

Should you actually want to step through a run of numbers, the built-in [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) function is convenient. It produces arithmetic progressions:

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4

```

The stated end value is left out of the produced sequence; `range(10)` yields 10 numbers, exactly the valid indices for a sequence holding 10 items. You can also have the range begin at a different number, or hand it another increment (including a negative one, occasionally referred to as the ‘step’):

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]

```

When you want to walk over the indices belonging to a sequence, pair [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) with [`len()`](https://docs.python.org/3.14/library/functions.html#len) in this manner:

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb

```

For the majority of these situations, though, the [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) function is the handier choice; refer to [Looping Techniques](https://docs.python.org/3.14/tutorial/datastructures.html#tut-loopidioms).

Something curious occurs when you simply print a range:

```python
>>> range(10)
range(0, 10)

```

The thing handed back by [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) acts in many respects like a list, yet it really isn’t one. As you iterate over it, it hands back the next item of the intended sequence one at a time, but it never actually constructs the list, which conserves memory.

Objects of this kind we call [iterable](https://docs.python.org/3.14/glossary.html#term-iterable): they can serve as a target for any function or construct that expects to pull items from a source one after another until none remain. The [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement, as we’ve seen, is one such construct; [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) illustrates a function that accepts an iterable:

```python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6

```

Further along we’ll meet additional functions that hand back iterables and accept iterables as their inputs. The [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) function gets fuller treatment within the [Data Structures](https://docs.python.org/3.14/tutorial/datastructures.html#tut-structures) chapter.

[Subject index](INDEX.md) · [Previous source section](for-statements.md) · [Following source section](break-and-continue-statements.md)
