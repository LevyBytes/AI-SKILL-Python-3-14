# collections: `collections.Counter`

### `Counter` objects

For quick and easy tallying, a counter tool is included. As an illustration:

```python
>>> # Tally occurrences of words in a list
>>> cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
...
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

>>> # Find the ten most common words in Hamlet
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

```

 *class *collections.Counter(***kwargs*)

 *class *collections.Counter(*iterable*, */*, ***kwargs*)

 *class *collections.Counter(*mapping*, */*, ***kwargs*)

A `Counter` is a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) subclass meant for tallying [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) objects. In this collection, the elements live as dictionary keys while their tallies live as dictionary values. A count may take on any integer value, zero and negatives included. The `Counter` class resembles the bags or multisets found in other languages.

You count elements from an *iterable* or set them up from a separate *mapping* (or counter):

```python
>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

```

Counter objects present a dictionary interface, with one difference: a missing item yields a zero count rather than raising a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError):

```python
>>> c = Counter(['eggs', 'ham'])
>>> c['bacon']                              # count of a missing element is zero
0

```

Assigning a count of zero will not drop an element from a counter. To get rid of it completely, use `del`:

```python
>>> c['sausage'] = 0                        # counter entry with a zero count
>>> del c['sausage']                        # del actually removes the entry

```

Added in version 3.1.

Changed in version 3.7: Being a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) subclass, `Counter` picked up the ability to retain insertion order. Math operations across *Counter* objects keep order intact as well. The ordering of results follows the point at which an element first shows up in the left operand, and after that the sequence met in the right operand.

On top of what all dictionaries offer, Counter objects come with extra methods:

[Subject index](INDEX.md) · [Previous](chainmap-examples-and-recipes.md) · [Continue](counter-elements-and-frequency-methods.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)
