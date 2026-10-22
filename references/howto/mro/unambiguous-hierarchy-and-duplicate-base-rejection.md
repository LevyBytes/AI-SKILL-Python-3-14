# Unambiguous hierarchy and duplicate-base rejection

The genuine fix is to lay out a non-ambiguous hierarchy — that is, to derive G from E and F (putting the more specific one first) instead of from F and E; done that way, the MRO is unmistakably GEF.

>

```text
           O
           |
           F (spam)
         / |
(eggs)   E |
         \ |
           G
             (eggs, no doubt)

```

Python 2.3 compels the programmer to compose good hierarchies (or, at the very least, ones that are less error-prone).

On a related point, let me mention that the Python 2.3 algorithm is clever enough to catch glaring mistakes, such as repeating a class within the list of parents:

```python
>>> class A(object): pass
>>> class C(A,A): pass # error
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: duplicate base class A

```

Python 2.2 (covering classic classes and new style classes alike), in the same situation, would throw no exception whatsoever.

To close, I'd like to draw out two lessons this example has taught us:

1.

its name notwithstanding, the MRO governs the resolution order of attributes, not methods alone;

2.

the default food for Pythonistas is spam ! (but you already knew that ;-)

[Subject index](INDEX.md) · [Historical local-precedence failures](historical-local-precedence-failures.md) · [Classic and Python 2.2 monotonicity failures](classic-and-python-2-2-monotonicity-failures.md) · [Previous source context](historical-local-precedence-failures.md) · [Following source context](classic-and-python-2-2-monotonicity-failures.md)
