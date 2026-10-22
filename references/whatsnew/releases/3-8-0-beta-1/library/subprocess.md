# Python 3.8.0 beta 1 / library / subprocess

[bpo-31961](https://bugs.python.org/issue?@action=redirect&bpo=31961): Brought bytes and path-like object support to [`subprocess.Popen()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) on Windows. When *shell* is `False`, the *args* parameter now takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) along with a sequence holding bytes and path-like objects. The *executable* parameter now takes a bytes and path-like object. The *cwd* parameter now takes a bytes object. Built on a patch from Anders Lorentsen.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
