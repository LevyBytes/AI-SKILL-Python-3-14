# Python 3.11.0 alpha 1 / core and builtins / collections and iteration

[bpo-34561](https://bugs.python.org/issue?@action=redirect&bpo=34561): Sorting a list now applies the merge-ordering approach drawn from Munro and Wild’s `powersort()`. In contrast to the previous approach, this one is provably near-optimal with respect to the entropy of the run-length distribution. The majority of `list.sort()` calls will likely not notice a meaningful timing change, yet may gain considerably where the old approach behaved especially badly. Still, since every one of these are quick linear-time approximations to a problem that is at best quadratic-time to solve perfectly, one can also construct cases where the older approach came out ahead.

[bpo-44821](https://bugs.python.org/issue?@action=redirect&bpo=44821): Build instance dictionaries (__dict__) eagerly, which makes object layout more uniform and aids specialization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
