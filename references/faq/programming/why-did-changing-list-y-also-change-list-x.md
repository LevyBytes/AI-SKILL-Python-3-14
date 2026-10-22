# Why did changing list ‘y’ also change list ‘x’?

### Why did changing list ‘y’ also change list ‘x’?

Should you write code such as:

```python
>>> x = []
>>> y = x
>>> y.append(10)
>>> y
[10]
>>> x
[10]

```

you may be puzzled about why appending an element to `y` altered `x` as well.

Two factors combine to bring about this outcome:

1.

Variables are nothing more than names pointing at objects. Performing `y = x` makes no copy of the list – it makes a new variable `y` that points at the very same object `x` points at. So there is just one object (the list), and `x` and `y` both point at it.

2.

Lists are [mutable](https://docs.python.org/3.14/glossary.html#term-mutable), which means that you can change their content.

Following the [`append()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.append) call, the content of the mutable object has gone from `[]` to `[10]`. Because both variables point at the same object, either name reaches the updated value `[10]`.

If we instead assign an immutable object to `x`:

```python
>>> x = 5  # ints are immutable
>>> y = x
>>> x = x + 1  # 5 can't be mutated, we are creating a new object here
>>> x
6
>>> y
5

```

we can observe that here `x` and `y` are no longer equal. The reason is that integers are [immutable](https://docs.python.org/3.14/glossary.html#term-immutable), and when we run `x = x + 1` we aren't mutating the int `5` by bumping up its value; rather, we are making a new object (the int `6`) and binding it to `x` (in other words, switching which object `x` points at). Once that assignment is done we have two objects (the ints `6` and `5`) plus two variables pointing at them (`x` now points at `6` while `y` still points at `5`).

Certain operations (such as `y.append(10)` and `y.sort()`) mutate the object, while operations that look similar on the surface (such as `y = y + [10]` and [`sorted(y)`](https://docs.python.org/3.14/library/functions.html#sorted)) build a new object. Broadly across Python (and in every case in the standard library) a method that mutates an object returns `None` to help keep the two kinds of operation from being mixed up. So if you mistakenly write `y.sort()` expecting it to hand you a sorted copy of `y`, you'll instead wind up with `None`, which will probably make your program throw an easily diagnosed error.

That said, there's one family of operations where the identical operation occasionally behaves differently across types: the augmented assignment operators. Take `+=`, which mutates a list yet not a tuple or an int (since `a_list += [1, 2, 3]` amounts to `a_list.extend([1, 2, 3])`, mutating `a_list`, while in contrast `some_tuple += (1, 2, 3)` along with `some_int += 1` build fresh objects).

Put differently:

- When we hold a mutable object (such as [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set)), we can apply certain operations to mutate it, and every variable pointing at it will observe the change.

- When we hold an immutable object (such as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)), every variable pointing at it will always observe the same value, but operations that turn that value into a new value always hand back a new object.

To learn whether two variables point at the same object or not, you can apply the [`is`](https://docs.python.org/3.14/reference/expressions.html#is) operator, or the built-in [`id()`](https://docs.python.org/3.14/library/functions.html#id) function.

[Subject index](INDEX.md)
