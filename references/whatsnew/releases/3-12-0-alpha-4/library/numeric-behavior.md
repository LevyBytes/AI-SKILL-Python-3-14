# Python 3.12.0 alpha 4 / library / numeric behavior

[gh-99925](https://github.com/python/cpython/issues/99925): Align the error messages produced during JSON serialization by `json.dumps(float('nan'), allow_nan=False)` and `json.dumps(float('nan'), allow_nan=False, indent=<SOMETHING>)`. Each now carries the representation of the offending value that could not be serialized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
