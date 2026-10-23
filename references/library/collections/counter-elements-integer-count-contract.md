# collections`Counter` objects - Contract: The `elements()` method calls for integer counts.

The `elements()` method calls for integer counts. Zero and negative counts are skipped.

See also

- [Bag class](https://www.gnu.org/software/smalltalk/manual-base/html_node/Bag.html) in Smalltalk.

- Wikipedia entry for [Multisets](https://en.wikipedia.org/wiki/Multiset).

- [C++ multisets](http://www.java2s.com/Tutorial/Cpp/0380__set-multiset/Catalog0380__set-multiset.htm) tutorial with examples.

- For a treatment of multiset math and where it applies, consult Knuth, Donald — see *The Art of Computer Programming*, Volume II, within *Section 4.6.3, Exercise 19*.

- To list every distinct multiset of a chosen size drawn from a chosen set of elements, turn to [`itertools.combinations_with_replacement()`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations_with_replacement):

```python
map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC

```

[Subject index](INDEX.md) · [Previous](collections-counter-update-to-collections-counter-update.md) · [Continue](collections-deque-class.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.Counter; collections.Counter; collections.Counter](collections-counter-class-to-collections-counter-class.md) · [Owning module, declaration or section: `Counter` objects](collections-counter-class-to-collections-counter-class.md) · [Owning module, declaration or section: update; update; update](collections-counter-update-to-collections-counter-update.md)
