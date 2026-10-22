# 5.4. Sets

### 5.4. Sets

Python ships a data type for [sets](https://docs.python.org/3.14/library/stdtypes.html#types-set) as well. A set is an unordered collection holding no duplicate elements. Among its basic uses are membership testing and stripping out duplicate entries. Set objects further support mathematical operations including union, intersection, difference, and symmetric difference.

You can build sets with curly braces or the [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) function. Note: building an empty set demands `set()` rather than `{}`; that latter form yields an empty dictionary, a data structure taken up in the section to come.

Since sets carry no order, iterating across them or printing them may surface the elements in some order other than you anticipate.

A short demonstration follows:

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
>>>
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

```

Much like list comprehensions, set comprehensions get support too:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}

```

[Subject index](INDEX.md) · [Previous source section](tuples-and-sequences.md) · [Following source section](dictionaries.md)
