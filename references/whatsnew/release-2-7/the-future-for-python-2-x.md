# What’s New in Python 2.7 / The Future for Python 2.x - argparse, collections, decimal, unittest

### What’s New in Python 2.7

Author:

A.M. Kuchling (amk at amk.ca)

The features introduced in Python 2.7 are described in this article. The release date of Python 2.7 was July 3, 2010.

Across many areas, numeric handling received improvements, covering both the [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) class and floating-point values. The standard library gained several handy additions: a substantially expanded [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module, the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module that parses command-line options, the practical [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) and [`Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter) classes within the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module, along with numerous further refinements.

Because Python 2.7 was intended to be the final 2.x release, effort went into ensuring it would serve well over the long term. Several features drawn from the Python 3.x line were brought into 2.7 to ease the transition toward Python 3.

Rather than supplying a full specification of every new capability, this article offers a handy summary. To get complete details, consult the Python 2.7 documentation at [https://docs.python.org](https://docs.python.org). When you need the reasoning behind a particular feature’s design and implementation, look at that feature’s PEP or the discussion of the change in its issue on [https://bugs.python.org](https://bugs.python.org). Wherever it can, “What’s New in Python” provides a link to the bug/patch entry for each change.

### The Future for Python 2.x

The final major version in the 2.x series is Python 2.7, since the Python maintainers redirected their efforts toward developing new features in the Python 3.x line. As a result, although Python 2 still gets bug fixes and updates so it keeps building correctly on fresh hardware and newer releases of supported operating systems, no further full feature releases will appear for either the language or the standard library.

That said, even though Python 2.7 and Python 3 share a sizable common subset—and although much of the work in moving to that common subset, or straight to Python 3, can be safely automated—certain other changes (particularly the ones tied to Unicode handling) may demand careful thought, and ideally solid automated regression test suites, in order to migrate successfully.

Consequently, Python 2.7 will stay around for a long time, serving as a stable, supported foundation for production systems that have not yet made the move to Python 3. [**PEP 373**](https://peps.python.org/pep-0373/) lays out the complete expected lifecycle of the Python 2.7 series.

A few important results of 2.7’s long-term importance are:

- As mentioned earlier, the 2.7 release enjoys a far longer maintenance window than the earlier 2.x versions did. The core development team is currently expected to keep supporting Python 2.7 (delivering security updates and other bug fixes) until 2020 at the earliest (a decade after its first release, versus the more usual 18–24 month support span).

- As the Python 2.7 standard library grows older, it becomes increasingly valuable for Python 2 users to make good use of the Python Package Index (whether directly or through a redistributor). Beyond a broad range of third-party packages addressing many tasks, the available packages encompass backports of fresh modules and features from the Python 3 standard library that work with Python 2, plus assorted tools and libraries that ease migration to Python 3. The [Python Packaging User Guide](https://packaging.python.org) offers instructions for downloading and installing software from the Python Package Index.

- While publishing new packages on the Python Package Index is now the favored way to extend Python 2, that route won’t always work, particularly for matters of network security. In rare situations that publishing new or updated packages on PyPI cannot adequately address, the Python Enhancement Proposal process can be invoked to argue for adding new features straight into the Python 2 standard library. Any additions of this kind, together with the maintenance releases in which they appeared, will be recorded in the New Features Added to Python 2.7 Maintenance Releases section further down.

For projects looking to move from Python 2 to Python 3, or for library and framework authors aiming to support users on both Python 2 and Python 3, an assortment of tools and guides exists to help choose an appropriate strategy and handle some of the technical specifics. The suggested place to begin is the [How to port Python 2 Code to Python 3](https://docs.python.org/3.14/howto/pyporting.html#pyporting-howto) HOWTO guide.

[Subject index](INDEX.md) · [Next source section](changes-to-the-handling-of-deprecation-warnings.md)
