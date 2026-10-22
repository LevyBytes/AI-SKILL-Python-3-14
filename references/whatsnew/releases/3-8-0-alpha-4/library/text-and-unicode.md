# Python 3.8.0 alpha 4 / library / text and unicode

[bpo-30485](https://bugs.python.org/issue?@action=redirect&bpo=30485): By supplying a default namespace under an empty-string prefix, xml.etree.ElementTree path expressions can now skip the explicit namespace prefixes on tags (or the ?{namespace}tag? form).

[bpo-33461](https://bugs.python.org/issue?@action=redirect&bpo=33461): Supplying the `encoding` option to `json.loads` now triggers a `DeprecationWarning`. Matthias Bussonnier authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
