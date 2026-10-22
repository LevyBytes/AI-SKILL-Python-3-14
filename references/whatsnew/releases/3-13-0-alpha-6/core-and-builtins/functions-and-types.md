# Python 3.13.0 alpha 6 / core and builtins / functions and types

[gh-116968](https://github.com/python/cpython/issues/116968): Add a single shared 16-bit backoff counter type (`_Py_BackoffCounter`), used by both the Tier 1 adaptive specializer and the Tier 2 optimizer. While the API for adaptive specialization counters shifts, the behavior is meant to stay the same.

How the Tier 2 counters act is now different:

  - Dynamic thresholds are gone (these were never actually varied).

  - Every counter shares one exponential backoff scheme now.

  - For `JUMP_BACKWARD`, the counter begins its countdown at 16.

  - Within side exits, the `temperature` begins its countdown at 64.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
