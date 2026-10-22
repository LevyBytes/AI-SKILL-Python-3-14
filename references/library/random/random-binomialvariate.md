# random — Discrete distributions

### Discrete distributions

The function below produces a discrete distribution.

 random.binomialvariate(*n=1*, *p=0.5*)

[Binomial distribution](https://mathworld.wolfram.com/BinomialDistribution.html). Hand back the count of successes across *n* independent trials when the chance of success on each trial is *p*:

Mathematically equivalent to:

```python
sum(random() < p for i in range(n))

```

The trial count *n* must be a non-negative integer. The success probability *p* must satisfy `0.0 <= p <= 1.0`. The outcome is an integer within the range `0 <= X <= n`.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](random-choice-to-random-sample.md) · [Continue](random-random-to-random-weibullvariate.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)
