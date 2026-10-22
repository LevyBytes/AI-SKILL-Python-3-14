# How fast are exceptions?

### How fast are exceptions?

When no exceptions get raised, a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)/[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) block is extremely efficient. The actual catching of an exception, by contrast, is costly. With Python releases before 2.0 it was common to reach for this idiom:

```python
try:
    value = mydict[key]
except KeyError:
    mydict[key] = getvalue(key)
    value = mydict[key]

```

This was only sensible when you anticipated the dict holding the key nearly every time. When that wasn't so, you'd write it this way instead:

```python
if key in mydict:
    value = mydict[key]
else:
    value = mydict[key] = getvalue(key)

```

For this particular scenario, `value = dict.setdefault(key, getvalue(key))` is also an option, but only when the `getvalue()` call is cheap enough, since it runs in every case.

[Subject index](INDEX.md)
