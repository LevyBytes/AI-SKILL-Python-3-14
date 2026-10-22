# Python 3.14.0 alpha 1 / library / collections and iteration

[gh-123884](https://github.com/python/cpython/issues/123884): Repaired a defect in itertools.tee() around handling tee inputs nested inside another tee (a tee within a tee). What comes out now delivers the promised *n* fresh, independent iterators. Previously the leading iterator matched (rather than being separate from) the source iterator. That occasionally produced unexpected outcomes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
