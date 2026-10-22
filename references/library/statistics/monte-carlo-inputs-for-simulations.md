# statistics — Monte Carlo inputs for simulations

### Monte Carlo inputs for simulations

When a model resists a tidy analytic solution, `NormalDist` can produce the input samples that feed a [Monte Carlo simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method) to approximate its distribution:

```pycon
>>> def model(x, y, z):
...     return (3*x + 7*x*y - 5*y) / (11 * z)
...
>>> n = 100_000
>>> X = NormalDist(10, 2.5).samples(n, seed=3652260728)
>>> Y = NormalDist(15, 1.75).samples(n, seed=4582495471)
>>> Z = NormalDist(50, 1.25).samples(n, seed=6582483453)
>>> quantiles(map(model, X, Y, Z))
[1.4591308524824727, 1.8035946855390597, 2.175091447274739]

```

[Subject index](INDEX.md) · [Previous](classic-probability-problems.md) · [Continue](approximating-binomial-distributions.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md)
