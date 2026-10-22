# The C3 Method Resolution Order

### The C3 Method Resolution Order

Let me set out a few straightforward notations that will help in the discussion ahead. I'll adopt the shorthand:

```python
C1 C2 ... CN

```

to indicate the list of classes [C1, C2, … , CN].

The *head* of the list is its first element:

```python
head = C1

```

whereas the *tail* is the rest of the list:

```python
tail = C2 ... CN.

```

I shall also use the notation:

```python
C + (C1 C2 ... CN) = C C1 C2 ... CN

```

to denote the sum of the lists [C] + [C1, C2, … ,CN].

Now I can explain how the MRO works in Python 2.3.

Picture a class C within a multiple inheritance hierarchy, where C draws from the base classes B1, B2, … , BN. Our aim is to work out the linearization L[C] of the class C, and the rule goes like this:

>

*C's linearization equals C added to the merge of the parents' linearizations together with the parents' own list.*

In symbolic notation:

```python
L[C(B1 ... BN)] = C + merge(L[B1] ... L[BN], B1 ... BN)

```

As a special case, when C is the `object` class — which has no parents at all — its linearization is trivial:

```python
L[object] = object.

```

In the general case, though, you'll need to work out the merge by following this recipe:

>

*grab the head of the first list, namely L[B1][0]; should that head appear in the tail of none of the remaining lists, append it to C's linearization and strip it from every list in the merge — otherwise turn to the head of the next list and take it instead, provided it qualifies as a good head. Keep repeating this until each class has been removed or no good head can be found anywhere. In the latter situation the merge cannot be built, Python 2.3 will decline to create the class C, and an exception will be raised.*

This recipe guarantees that the merge operation *keeps* the ordering intact whenever the ordering can be kept. But where the order can't be kept — as in the case of serious order disagreement covered above — the merge simply can't be worked out.

Working out the merge is trivial when C has just a single parent (single inheritance); in that situation:

```python
L[C(B)] = C + merge(L[B],B) = C + L[B]

```

With multiple inheritance, on the other hand, matters get messier, and I wouldn't expect the rule to click for you absent a couple of examples ;-)

[Subject index](INDEX.md) · [Previous source context](the-beginning.md) · [Following source context](first-c3-hierarchy-and-base-class-merge.md)
