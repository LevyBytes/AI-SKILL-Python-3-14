# How can I sort one list by values from another list?

### How can I sort one list by values from another list?

Combine them into an iterator of tuples, sort that combined list, and finally extract the piece you care about.

```python
>>> list1 = ["what", "I'm", "sorting", "by"]
>>> list2 = ["something", "else", "to", "sort"]
>>> pairs = zip(list1, list2)
>>> pairs = sorted(pairs)
>>> pairs
[("I'm", 'else'), ('by', 'sort'), ('sorting', 'to'), ('what', 'something')]
>>> result = [x[1] for x in pairs]
>>> result
['else', 'sort', 'to', 'something']

```

[Subject index](INDEX.md)
