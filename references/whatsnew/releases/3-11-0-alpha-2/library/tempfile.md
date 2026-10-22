# Python 3.11.0 alpha 2 / library / tempfile

[bpo-45192](https://bugs.python.org/issue?@action=redirect&bpo=45192): Repair the `tempfile._infer_return_type` function so the `dir` argument given to the [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile) functions takes an object that implements the `os.PathLike` protocol.

Kyungmin Lee wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
