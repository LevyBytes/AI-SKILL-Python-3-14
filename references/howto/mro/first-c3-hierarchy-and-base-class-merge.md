# First C3 hierarchy and base-class merge

### Examples

First example. Consider the following hierarchy:

```python
>>> O = object
>>> class F(O): pass
>>> class E(O): pass
>>> class D(O): pass
>>> class C(D,F): pass
>>> class B(D,E): pass
>>> class A(B,C): pass

```

In this case the inheritance graph can be drawn as:

>

```text
                          6
                         ---
Level 3                 | O |                  (more general)
                      /  ---  \
                     /    |    \                      |
                    /     |     \                     |
                   /      |      \                    |
                  ---    ---    ---                   |
Level 2        3 | D | 4| E |  | F | 5                |
                  ---    ---    ---                   |
                   \  \ _ /       |                   |
                    \    / \ _    |                   |
                     \  /      \  |                   |
                      ---      ---                    |
Level 1            1 | B |    | C | 2                 |
                      ---      ---                    |
                        \      /                      |
                         \    /                      \ /
                           ---
Level 0                 0 | A |                (more specialized)
                           ---

```

The linearizations of O,D,E and F are trivial:

```python
L[O] = O
L[D] = D O
L[E] = E O
L[F] = F O

```

The linearization of B can be computed as:

```python
L[B] = B + merge(DO, EO, DE)

```

D turns out to be a good head, so we pick it, leaving us to evaluate `merge(O,EO,E)`. At this point O fails to be a good head, because it sits in the tail of the sequence EO. The rule then tells us to move on to the next sequence. E now qualifies as a good head; we take it, and what's left to evaluate is `merge(O,O)`, which yields O. Hence:

```python
L[B] =  B D E O

```

Using the same procedure one finds:

```python
L[C] = C + merge(DO,FO,DF)
     = C + D + merge(O,FO,F)
     = C + D + F + merge(O,O)
     = C D F O

```

[Subject index](INDEX.md) · [Derived C3 merge and second hierarchy exercise](derived-c3-merge-and-second-hierarchy-exercise.md) · [Conflicting base orders cannot be merged](conflicting-base-orders-cannot-be-merged.md) · [Previous source context](the-c3-method-resolution-order.md) · [Following source context](derived-c3-merge-and-second-hierarchy-exercise.md)
