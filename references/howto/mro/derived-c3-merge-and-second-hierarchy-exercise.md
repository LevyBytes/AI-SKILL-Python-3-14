# Derived C3 merge and second hierarchy exercise

Now we can compute:

```python
L[A] = A + merge(BDEO,CDFO,BC)
     = A + B + merge(DEO,CDFO,C)
     = A + B + C + merge(DEO,DFO)
     = A + B + C + D + merge(EO,FO)
     = A + B + C + D + E + merge(O,FO)
     = A + B + C + D + E + F + merge(O,O)
     = A B C D E F O

```

For this example the linearization lines up rather neatly with the inheritance level, meaning the lower levels (the more specialized classes, that is) end up with higher precedence (have a look at the inheritance graph). That tidiness, however, doesn't hold in general.

Computing the linearization for my second example I'll leave to the reader as an exercise:

```python
>>> O = object
>>> class F(O): pass
>>> class E(O): pass
>>> class D(O): pass
>>> class C(D,F): pass
>>> class B(E,D): pass
>>> class A(B,C): pass

```

All that sets this apart from the earlier example is swapping B(D,E) –> B(E,D); yet even so small a tweak overturns the hierarchy's ordering entirely:

>

```text
                           6
                          ---
Level 3                  | O |
                       /  ---  \
                      /    |    \
                     /     |     \
                    /      |      \
                  ---     ---    ---
Level 2        2 | E | 4 | D |  | F | 5
                  ---     ---    ---
                   \      / \     /
                    \    /   \   /
                     \  /     \ /
                      ---     ---
Level 1            1 | B |   | C | 3
                      ---     ---
                       \       /
                        \     /
                          ---
Level 0                0 | A |
                          ---

```

Observe how the class E, sitting at the hierarchy's second level, comes ahead of the class C, which sits at the first level — in other words E counts as more specialized than C despite occupying a higher level.

A lazy programmer can read off the MRO straight from Python 2.2, given that here it matches the Python 2.3 linearization. Simply call the [`mro()`](https://docs.python.org/3.14/reference/datamodel.html#type.mro) method on class A:

```python
>>> A.mro()
[<class 'A'>, <class 'B'>, <class 'E'>,
<class 'C'>, <class 'D'>, <class 'F'>,
<class 'object'>]

```

[Subject index](INDEX.md) · [First C3 hierarchy and base-class merge](first-c3-hierarchy-and-base-class-merge.md) · [Conflicting base orders cannot be merged](conflicting-base-orders-cannot-be-merged.md) · [Previous source context](first-c3-hierarchy-and-base-class-merge.md) · [Following source context](conflicting-base-orders-cannot-be-merged.md)
