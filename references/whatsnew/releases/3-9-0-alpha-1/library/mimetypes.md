# Python 3.9.0 alpha 1 / library / mimetypes

[bpo-38449](https://bugs.python.org/issue?@action=redirect&bpo=38449): PR 15522 was reverted because it caused a regression in [`mimetypes.guess_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_type) stemming from filenames being mishandled as urls.

[bpo-4963](https://bugs.python.org/issue?@action=redirect&bpo=4963): Eliminate non-deterministic behavior tied to mimetypes extension mapping together with module reinitialization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
