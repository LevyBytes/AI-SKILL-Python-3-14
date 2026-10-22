# re: `re.Match`

### Match Objects

Match objects carry a boolean value of `True` at all times. Given that `match()` and `search()` give back `None` when nothing matches, a plain `if` statement lets you check whether a match happened:

```python
match = re.search(pattern, string)
if match:
    process(match)

```

 *class *re.Match

Match object returned by successful `match`es and `search`es.

[Subject index](INDEX.md) · [Previous](pattern-pattern.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Required continuation of the source contract](match-expand-to-match-group.md)
