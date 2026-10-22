# Python 3.8.0 alpha 1 / library / select

[bpo-35310](https://bugs.python.org/issue?@action=redirect&bpo=35310): Corrected a defect in [`select.select()`](https://docs.python.org/3.14/library/select.html#select.select) whereby, under certain conditions, the file descriptor sequences came back unchanged following a signal interruption, despite the descriptors possibly not being ready yet. Going forward, `select.select()` always hands back empty lists once a timeout has elapsed. Patch by Oran Avraham.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
