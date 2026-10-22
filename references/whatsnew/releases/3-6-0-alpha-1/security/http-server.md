# Python 3.6.0 alpha 1 / security / http server

[bpo-26657](https://bugs.python.org/issue?@action=redirect&bpo=26657): Close a directory traversal hole affecting http.server on Windows. The regression being repaired had entered the tree in 3.3.4rc1 and 3.4.0rc1. Philipp Hagemeister's patch served as the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
