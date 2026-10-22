# Python 3.8.0 beta 1 / library / codecs

[bpo-33361](https://bugs.python.org/issue?@action=redirect&bpo=33361): Fixes a defect in [`codecs.StreamRecoder`](https://docs.python.org/3.14/library/codecs.html#codecs.StreamRecoder) whereby a seek could leave stale data sitting in a buffer and spoil later read calls. Ammar Askar supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
