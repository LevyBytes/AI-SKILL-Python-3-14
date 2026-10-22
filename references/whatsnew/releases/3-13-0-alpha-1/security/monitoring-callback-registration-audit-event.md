# Python 3.13.0 alpha 1 / security / according pep sys monitoring register callback supposed emit audit event

[gh-107774](https://github.com/python/cpython/issues/107774): According to PEP 669, `sys.monitoring.register_callback` is supposed to emit an audit event. That audit event was absent in the pre-releases of Python 3.12, and the gap is now closed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
