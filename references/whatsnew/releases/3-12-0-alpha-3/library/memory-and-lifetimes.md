# Python 3.12.0 alpha 3 / library / memory and lifetimes

[gh-99240](https://github.com/python/cpython/issues/99240): Eliminate a double-free defect in the Argument Clinic `str_converter` by moving memory teardown into a fresh `post_parsing` section.

[gh-64490](https://github.com/python/cpython/issues/64490): Correct a refcount error that occurred when arguments get packed into a tuple in Argument Clinic.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
