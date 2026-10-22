# Conflicting base orders cannot be merged

Lastly, let me revisit the example from the first section, the one with a serious order disagreement. Here the linearizations of O, X, Y, A and B are easy enough to work out:

>

```text
L[O] = 0
L[X] = X O
L[Y] = Y O
L[A] = A X Y O
L[B] = B Y X O

```

Working out the linearization for a class C that inherits from both A and B, however, turns out to be impossible:

```python
L[C] = C + merge(AXYO, BYXO, AB)
     = C + A + merge(XYO, BYXO, B)
     = C + A + B + merge(XYO, YXO)

```

From here the lists XYO and YXO refuse to merge: X lives in the tail of YXO while Y lives in the tail of XYO, so no good heads exist and the C3 algorithm halts. Python 2.3 throws an error and declines to create the class C.

[Subject index](INDEX.md) · [First C3 hierarchy and base-class merge](first-c3-hierarchy-and-base-class-merge.md) · [Derived C3 merge and second hierarchy exercise](derived-c3-merge-and-second-hierarchy-exercise.md) · [Previous source context](derived-c3-merge-and-second-hierarchy-exercise.md) · [Following source context](historical-local-precedence-failures.md)
