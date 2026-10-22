# Why does Python allow commas at the end of lists and tuples?

### Why does Python allow commas at the end of lists and tuples?

In Python you are free to place a trailing comma after the final item of lists, tuples, and dictionaries:

```python
[1, 2, 3,]
('a', 'b', 'c',)
d = {
    "A": [1, 5],
    "B": [6, 7],  # last trailing comma is optional but good style
}

```

Permitting this serves a handful of purposes.

Whenever a list, tuple, or dictionary literal stretches over several lines, tacking on extra elements becomes simpler, since you needn’t recall to append a comma onto the line above. On top of that, you can shuffle the lines around without provoking a syntax error.

Leaving the comma out by mistake can produce bugs that prove tricky to track down. Consider:

```python
x = [
  "fee",
  "fie"
  "foo",
  "fum"
]

```

At a glance the list appears to hold four items, yet it really holds only three: “fee”, “fiefoo” and “fum”. Making a habit of including the comma sidesteps this pitfall entirely.

Beyond that, permitting the trailing comma can smooth the path for code that is generated programmatically.

[Subject index](INDEX.md)
