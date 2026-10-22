# Comparison Functions

### Comparison Functions

Whereas a key function yields one standalone value for each item, a comparison function instead works out how two given inputs rank relative to each other.

Picture a [balance scale](https://upload.wikimedia.org/wikipedia/commons/1/17/Balance_à_tabac_1850.JPG), which weighs two samples and reports their relative standing: lighter, equal, or heavier. In the same spirit, a comparison function written as `cmp(a, b)` yields a negative number for less-than, zero when the two inputs match, and a positive number for greater-than.

You will often run across comparison functions while porting algorithms over from other languages. Beyond that, certain libraries expose comparison functions within their API; [`locale.strcoll()`](https://docs.python.org/3.14/library/locale.html#locale.strcoll), for one, is such a function.

So that these cases are covered, Python offers [`functools.cmp_to_key`](https://docs.python.org/3.14/library/functools.html#functools.cmp_to_key), which wraps a comparison function so it can act as a key function:

```python
sorted(words, key=cmp_to_key(strcoll))  # locale-aware sort order

```

[Subject index](INDEX.md) · [Previous source context](decorate-sort-undecorate.md) · [Following source context](strategies-for-unorderable-types-and-values.md)
