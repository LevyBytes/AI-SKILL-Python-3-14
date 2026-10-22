# re — Finding all Adverbs and their Positions

### Finding all Adverbs and their Positions

When you need richer detail about every match of a pattern than the matched text alone, `finditer()` helps, since it yields `Match` objects in place of strings. Picking up from the earlier example, a writer hoping to find each adverb *and their positions* in some text would call `finditer()` like so:

```python
>>> text = "He was carefully disguised but captured quickly by police."
>>> for m in re.finditer(r"\w+ly\b", text):
...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
07-16: carefully
40-47: quickly

```

[Subject index](INDEX.md) · [Previous](finding-all-adverbs.md) · [Continue](raw-string-notation.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
