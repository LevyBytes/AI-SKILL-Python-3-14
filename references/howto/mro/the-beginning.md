# The beginning

### The beginning

>

*Felix qui potuit rerum cognoscere causas* – Virgilius

It all began with a message Samuele Pedroni sent to the Python development mailing list [1]. There, Samuele demonstrated that the Python 2.2 method resolution order fails to be monotonic, and he put forward the C3 method resolution order as a replacement. Guido found his reasoning persuasive, and so Python 2.3 now relies on C3. C3 as a method has no inherent connection to Python — it originated with people working on Dylan and is laid out in a paper written for lispers [2]. This paper here offers a (with luck) approachable treatment of the C3 algorithm aimed at Pythonistas curious about why the change was made.

To begin with, let me stress that everything I'm about to cover pertains solely to the *new style classes* that Python 2.2 brought in: *classic classes* keep their former method resolution order, which goes depth first and then left to right. So no old code breaks for classic classes; and although in theory some Python 2.2 new style class code could break, in practice the situations where the C3 resolution order diverges from the Python 2.2 method resolution order are so uncommon that no genuine breakage is anticipated. So:

>

*Don’t be scared!*

What's more, as long as you aren't leaning heavily on multiple inheritance with non-trivial hierarchies, there's no need to grasp the C3 algorithm, and you can comfortably skip over this paper. If, on the other hand, you genuinely want to learn how multiple inheritance operates, then this paper is meant for you. Happily, the subject turns out to be less involved than you might assume.

Let me open with a handful of basic definitions.

1.

Take a class C sitting in some tangled multiple inheritance hierarchy: pinning down the sequence in which methods get overridden — that is, fixing the order of C's ancestors — is no easy matter.

2.

When you take the ancestors of a class C — the class itself included — and arrange them from closest ancestor out to most distant, the resulting list goes by the name class precedence list, or the *linearization* of C.

3.

The *Method Resolution Order* (MRO) refers to the collection of rules from which the linearization is built. Throughout the Python literature, the phrase “the MRO of C” doubles as a synonym for the linearization of the class C.

4.

As an illustration, with a single inheritance hierarchy where C derives from C1 and C1 in turn derives from C2, the linearization of C comes out as nothing more than the list [C, C1 , C2]. Once multiple inheritance hierarchies enter the picture, though, building the linearization grows trickier, because producing one that honors both *local precedence ordering* and *monotonicity* is harder to pull off.

5.

Local precedence ordering I'll take up further on, but the definition of monotonicity I can supply right now. A MRO counts as monotonic precisely when this holds: *whenever C1 comes before C2 within C's linearization, C1 likewise comes before C2 within the linearization of every subclass of C*. Were that not so, the seemingly harmless act of deriving a fresh class might alter the order in which methods resolve, possibly seeding very subtle bugs. Cases of exactly this will be demonstrated later on.

6.

A linearization isn't something every class can have. Within complicated hierarchies you'll find cases where no class can be derived whose linearization satisfies every property you'd want.

Let me offer an example of just such a case. Take the hierarchy

```python
>>> O = object
>>> class X(O): pass
>>> class Y(O): pass
>>> class A(X,Y): pass
>>> class B(Y,X): pass

```

which the inheritance graph below depicts; there I've used O to stand for the `object` class, the root from which every new style class hierarchy springs:

>

```text
 -----------
|           |
|    O      |
|  /   \    |
 - X    Y  /
   |  / | /
   | /  |/
   A    B
   \   /
     ?

```

Here there's no way to derive a new class C out of A and B: X comes ahead of Y in A while Y comes ahead of X in B, so the method resolution order in C would be ambiguous.

Faced with this, Python 2.3 throws an exception (TypeError: MRO conflict among bases Y, X), barring the unwary programmer from constructing ambiguous hierarchies. Python 2.2, by contrast, throws nothing and instead settles on an *ad hoc* ordering (CABXYO here).

[Subject index](INDEX.md) · [Previous source context](the-python-2-3-method-resolution-order.md) · [Following source context](the-c3-method-resolution-order.md)
