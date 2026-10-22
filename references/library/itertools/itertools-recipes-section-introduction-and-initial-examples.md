# itertools — Itertools Recipes — Section introduction and initial examples

### Itertools Recipes

Below are recipes that build an extended toolset by treating the existing itertools as building blocks.

Education is the main goal of the itertools recipes. They illustrate different ways to think about each tool — for instance, that `chain.from_iterable` relates to the idea of flattening. They also suggest ways the tools combine — for instance, how `starmap()` and `repeat()` cooperate. On top of that, the recipes demonstrate patterns for pairing itertools with the [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) and [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) modules, plus the built-in itertools like `map()`, `filter()`, `reversed()`, and `enumerate()`.

A further role of the recipes is to act as an incubator. The `accumulate()`, `compress()`, and `pairwise()` itertools began life as recipes. At present the `sliding_window()`, `derangements()`, and `sieve()` recipes are under trial to determine whether they earn their place.

Nearly all of these recipes, along with many more, can be installed from the [more-itertools](https://pypi.org/project/more-itertools/) project on the Python Package Index:

```python
python -m pip install more-itertools

```

A lot of the recipes deliver the same strong performance as the toolset they rest on. Better memory behavior comes from handling elements one by one instead of loading an entire iterable into memory at once. The amount of code stays small by chaining the tools in a [functional style](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf). Speed is preserved by favoring “vectorized” building blocks over for-loops and [generators](https://docs.python.org/3.14/glossary.html#term-generator), which add interpreter overhead.

[Subject index](INDEX.md) · [Previous](itertools-zip-longest.md) · [Continue](itertools-recipes-shared-imports-and-basic-iterator-recipes.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md)
