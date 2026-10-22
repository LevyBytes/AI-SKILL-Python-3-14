# 10.6. Mathematics

### 10.6. Mathematics

Through the [`math`](https://docs.python.org/3.14/library/math.html#module-math) module you can reach the C library routines that back floating-point math:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0

```

For drawing random choices, the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module supplies the necessary tools:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float from the interval [0.0, 1.0)
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4

```

Fundamental statistical measures over numeric data — among them the mean, median, and variance — are computed by the [`statistics`](https://docs.python.org/3.14/library/statistics.html#module-statistics) module:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095

```

Numerous additional modules for numerical work are offered by the SciPy project at <[https://scipy.org](https://scipy.org)>.

[Subject index](INDEX.md) · [Previous source section](string-pattern-matching.md) · [Following source section](internet-access.md)
