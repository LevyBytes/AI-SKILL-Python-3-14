# Python 3.14.0 alpha 4 / library / getopt

[gh-126225](https://github.com/python/cpython/issues/126225): The [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt) and [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) modules no longer carry a deprecated marking. Sound reasons exist for choosing one of them over [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), and none of the three faces removal from the standard library. Among them, `argparse` stays the suggested default, *unless* one of the cautions listed at the head of the `optparse` module documentation is relevant.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
