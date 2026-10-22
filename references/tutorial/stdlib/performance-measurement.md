# 10.10. Performance measurement

### 10.10. Performance measurement

A portion of Python's audience becomes keenly curious about how various solutions to one problem stack up against each other in speed. To settle such questions on the spot, Python ships a measurement tool.

Consider, for instance, the lure of swapping arguments via tuple packing and unpacking rather than the conventional technique. A quick run through the [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) module reveals a small edge in speed:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791

```

Where [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) zooms in on tiny snippets, the [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile) and [`pstats`](https://docs.python.org/3.14/library/profile.html#module-pstats) modules instead help you spot the time-hungry regions within bigger stretches of code.

[Subject index](INDEX.md) · [Previous source section](data-compression.md) · [Following source section](quality-control.md)
