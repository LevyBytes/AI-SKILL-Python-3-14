# Python 3.13.0 alpha 3 / library / completed http response stream cleanup

[gh-113199](https://github.com/python/cpython/issues/113199): When the content length is known, `http.client.HTTPResponse.read1` and `http.client.HTTPResponse.readline` now shut the underlying IO once every byte has been consumed. Illia Volochii contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
