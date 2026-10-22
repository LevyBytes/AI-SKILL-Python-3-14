# difflib.SequenceMatcher: `set_seqs()`, `set_seq1()`, `set_seq2()`, `find_longest_match()`, `get_matching_blocks()`

set_seqs(*a*, *b*)

Set the two sequences that will be contrasted.

`SequenceMatcher` works out and caches thorough information about the second sequence, so when you intend to contrast one sequence against many, call `set_seq2()` once to fix the sequence used repeatedly and then call `set_seq1()` again and again, once per remaining sequence.

 set_seq1(*a*)

Set the first sequence that will be contrasted. The second sequence to be compared is not changed.

 set_seq2(*b*)

Set the second sequence that will be contrasted. The first sequence to be compared is not changed.

 find_longest_match(*alo=0*, *ahi=None*, *blo=0*, *bhi=None*)

Find longest matching block in `a[alo:ahi]` and `b[blo:bhi]`.

When *isjunk* was left out or was `None`, `find_longest_match()` returns `(i, j, k)` for which `a[i:i+k]` equals `b[j:j+k]`, with `alo <= i <= i+k <= ahi` and `blo <= j <= j+k <= bhi`. Across every `(i', j', k')` that satisfies those conditions, the further conditions `k >= k'`, `i <= i'`, and, when `i == i'`, `j <= j'` hold as well. Put differently, out of all the maximal matching blocks it returns one that begins soonest in *a*, and out of those maximal matching blocks beginning soonest in *a* it returns the one beginning soonest in *b*.

```python
>>> s = SequenceMatcher(None, " abcd", "abcd abcd")
>>> s.find_longest_match(0, 5, 0, 9)
Match(a=0, b=4, size=5)

```

When *isjunk* was supplied, the longest matching block is first found as above but with the extra rule that no junk element may sit inside the block. That block is then stretched as far as it will go by matching (only) junk elements on either side. Consequently the resulting block never matches on junk except where identical junk happens to lie next to an interesting match.

Below is the earlier example repeated, only now blanks are deemed junk. As a result, a direct pairing of `' abcd'` with the trailing `' abcd'` in the second sequence is blocked. What can pair instead is just the `'abcd'`, and it lines up with the leftmost `'abcd'` found in the second sequence:

```python
>>> s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
>>> s.find_longest_match(0, 5, 0, 9)
Match(a=1, b=0, size=4)

```

When nothing matches, this returns `(alo, blo, 0)`.

This method gives back a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `Match(a, b, size)`.

Changed in version 3.9: Added default arguments.

 get_matching_blocks()

Hand back a list of triples that describe the non-overlapping matching subsequences. Each triple takes the form `(i, j, n)` and signifies that `a[i:i+n] == b[j:j+n]`. The triples rise monotonically in *i* and *j*.

The final triple is a dummy carrying the value `(len(a), len(b), 0)`. It is the sole triple where `n == 0`. When `(i, j, n)` and `(i', j', n')` are neighboring triples in the list and the second is not the list's final triple, then `i+n < i'` or `j+n < j'`; that is, neighboring triples always describe non-adjacent equal blocks.

```pycon
>>> s = SequenceMatcher(None, "abxcd", "abcd")
>>> s.get_matching_blocks()
[Match(a=0, b=0, size=2), Match(a=3, b=2, size=2), Match(a=5, b=4, size=0)]

```

[Subject index](INDEX.md) · [Previous](difflib-sequencematcher-class.md) · [Continue](sequence-matcher-opcodes-and-similarity.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md) · [Owning module, declaration or section: difflib.SequenceMatcher](difflib-sequencematcher-class.md) · [Owning module, declaration or section: SequenceMatcher objects](difflib-sequencematcher-class.md)
