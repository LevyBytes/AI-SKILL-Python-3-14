# re - Finding all Adverbs

### Finding all Adverbs

`findall()` picks up *every* instance of a pattern rather than stopping at the first the way `search()` would. Suppose, for instance, a writer wished to locate all the adverbs within some text — they could call `findall()` like this:

```python
>>> text = "He was carefully disguised but captured quickly by police."
>>> re.findall(r"\w+ly\b", text)
['carefully', 'quickly']

```

[Subject index](INDEX.md) · [Previous](text-munging.md) · [Continue](finding-all-adverbs-and-their-positions.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
