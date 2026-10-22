# Classic and Python 2.2 monotonicity failures

With local precedence ordering now behind us, let me turn to the question of monotonicity. What I aim to establish is that neither the MRO for classic classes nor the one for Python 2.2 new style classes is monotonic.

Showing that the MRO for classic classes fails to be monotonic is fairly trivial — a glance at the diamond diagram suffices:

>

```text
   C
  / \
 /   \
A     B
 \   /
  \ /
   D

```

One easily discerns the inconsistency:

```python
L[B,P21] = B C        # B precedes C : B's methods win
L[D,P21] = D A C B C  # B follows C  : C's methods win!

```

By contrast, the Python 2.2 and 2.3 MROs run into no such trouble; both yield:

```python
L[D] = D A B C

```

In his essay [3] Guido notes that the classic MRO isn't all that bad in real use, since diamonds can usually be sidestepped with classic classes. Every new style class, however, inherits from `object`, which makes diamonds inescapable and lets inconsistencies surface in every multiple inheritance graph.

The Python 2.2 MRO makes breaking monotonicity hard, though not impossible. The example below, which Samuele Pedroni first supplied, shows the Python 2.2 MRO to be non-monotonic:

```python
>>> class A(object): pass
>>> class B(object): pass
>>> class C(object): pass
>>> class D(object): pass
>>> class E(object): pass
>>> class K1(A,B,C): pass
>>> class K2(D,B,E): pass
>>> class K3(D,A):   pass
>>> class Z(K1,K2,K3): pass

```

Below are the linearizations as the C3 MRO computes them (as an exercise, the reader ought to confirm these linearizations and sketch the inheritance diagram ;-)

```python
L[A] = A O
L[B] = B O
L[C] = C O
L[D] = D O
L[E] = E O
L[K1]= K1 A B C O
L[K2]= K2 D B E O
L[K3]= K3 D A O
L[Z] = Z K1 K2 K3 D A B C E O

```

For A, B, C, D, E, K1, K2 and K3 Python 2.2 returns precisely the same linearizations, yet for Z it returns a different one:

```python
L[Z,P22] = Z K1 K3 A K2 D B C E O

```

Plainly this linearization is *wrong*: A lands ahead of D here, whereas within the linearization of K3, A lands *after* D. Put differently, in K3 the methods coming from D override those coming from A, but in Z — still a subclass of K3 — the methods coming from A override those coming from D! That breaks monotonicity. Beyond that, the Python 2.2 linearization of Z also clashes with local precedence ordering, because the local precedence list of the class Z reads [K1, K2, K3] (with K2 ahead of K3), while in the linearization of Z, K2 *follows* K3. Failings like these are why the 2.2 rule was set aside in favor of the C3 rule.

### The end

This part is meant for the impatient reader who breezed past every preceding section and leapt straight to the finish. It's likewise for the lazy programmer who'd rather not put her/his brain to work. And it's for the programmer with a touch of hubris too — why else would s/he be reading a paper about the C3 method resolution order in multiple inheritance hierarchies ;-) Possessing all three of these virtues together (and *not* one at a time) earns a reward: a compact Python 2.2 script that lets you compute the 2.3 MRO without taxing your brain. Just edit the final line to experiment with the assorted examples I've gone over in this paper.:

That’s all folks,

>

enjoy !

### Resources

[Subject index](INDEX.md) · [Historical local-precedence failures](historical-local-precedence-failures.md) · [Unambiguous hierarchy and duplicate-base rejection](unambiguous-hierarchy-and-duplicate-base-rejection.md) · [Complete historical Python 2 C3 MRO implementation](complete-historical-python-2-c3-mro-implementation.md) · [Previous source context](unambiguous-hierarchy-and-duplicate-base-rejection.md) · [Following source context](complete-historical-python-2-c3-mro-implementation.md) · [Previous source context](complete-historical-python-2-c3-mro-implementation.md)
