# Python 3.14.0 alpha 1 / library / functional

[gh-118911](https://github.com/python/cpython/issues/118911): Within PyREPL, the logic of `maybe-accept` was revised so that pressing Enter twice lets the user close out the block even with trailing whitespace present. On top of that, pressing arrow up now leaves the cursor on the final functional line, which lines up with IPython's behavior. Aya Elsayed authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
