# difflib: `difflib.SequenceMatcher`

### `difflib` - Helpers for computing deltas

**Source code:** [Lib/difflib.py](https://github.com/python/cpython/tree/3.14/Lib/difflib.py)

---

The classes and functions exported by this module exist to compare sequences against one another. A typical use is contrasting files and emitting a report of their differences in several layouts — among them HTML as well as context and unified diffs. When the goal is to contrast whole directories and the files inside them, consult the [`filecmp`](https://docs.python.org/3.14/library/filecmp.html#module-filecmp) module as well.

 *class *difflib.SequenceMatcher

This is an adaptable class for matching up two sequences whose elements may be of any type, provided those elements are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). Its core algorithm came earlier than — and is somewhat more elaborate than — a method that Ratcliff and Obershelp put forward in the late 1980's under the grandiose label "gestalt pattern matching." The strategy is to locate the longest run of contiguous matching items that holds no "junk" elements; such "junk" elements are those judged uninteresting in some respect, like blank lines or whitespace. (Treating junk this way extends the original Ratcliff and Obershelp algorithm.) That very strategy is then reapplied recursively to whatever portions of the sequences lie to the left and to the right of the matched run. The result is not a minimal edit sequence, yet it tends to produce matches that people feel "look right."

**Timing:** In the worst case the underlying Ratcliff-Obershelp algorithm runs in cubic time, dropping to quadratic in the expected case. `SequenceMatcher` runs in quadratic time at worst, while its expected-case cost varies in an intricate way with the count of elements the two sequences share; at best it is linear.

**Automatic junk heuristic:** `SequenceMatcher` ships with a heuristic that flags some sequence items as junk on its own. The heuristic tallies the number of occurrences of each distinct item across the sequence. Once an item's repeats (everything past the first appearance) exceed 1% of the sequence and that sequence runs to 200 items or more, the item gets labeled "popular" and is treated as junk while matching proceeds. You can disable this heuristic by passing `False` for the `autojunk` argument as you build the `SequenceMatcher`.

Changed in version 3.2: Added the *autojunk* parameter.

### SequenceMatcher objects

The `SequenceMatcher` class is built by this constructor:

 *class *difflib.SequenceMatcher(*isjunk=None*, *a=''*, *b=''*, *autojunk=True*)

The optional argument *isjunk* must be either `None` (the default) or a one-argument function that receives a sequence element and returns true exactly when that element is "junk" and should be skipped. Handing `None` to *isjunk* amounts to handing `lambda x: False`; that is, nothing gets skipped. As an illustration, pass:

```python
lambda x: x in " \t"

```

when you are contrasting lines as sequences of characters and would rather not synch up on blanks or hard tabs.

The optional arguments *a* and *b* are the sequences to contrast; each defaults to an empty string. Both sequences' elements must be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

The optional argument *autojunk* lets you switch off the automatic junk heuristic.

Changed in version 3.2: Added the *autojunk* parameter.

SequenceMatcher objects carry three data attributes: *bjunk* is the set of *b* elements for which *isjunk* is `True`; *bpopular* is the set of non-junk elements the heuristic deems popular (when it has not been disabled); *b2j* is a dict that maps the remaining *b* elements to a list of the positions where they show up. All three get reset whenever *b* is reset through `set_seqs()` or `set_seq2()`.

Added in version 3.2: The *bjunk* and *bpopular* attributes.

`SequenceMatcher` objects expose the following methods:

[Subject index](INDEX.md) · [Continue](difflib-differ-class.md) · [Previous](difflib-diff-bytes-to-difflib-is-character-junk.md) · [Continue](sequence-matcher-inputs-and-matching-blocks.md)
