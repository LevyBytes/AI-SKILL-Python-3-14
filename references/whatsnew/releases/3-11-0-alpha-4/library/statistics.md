# Python 3.11.0 alpha 4 / library / statistics

[bpo-46257](https://bugs.python.org/issue?@action=redirect&bpo=46257): Tuned the mean, variance, and stdev functions inside the statistics module. When the input is an iterator, a single pass consumes it instead of burning memory by turning it into a list. That one-pass algorithm runs roughly twice as quickly as the earlier two-pass version.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
