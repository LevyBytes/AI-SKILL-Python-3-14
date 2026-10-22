# Python 3.10.0 alpha 6 / library / gzip

[bpo-43317](https://bugs.python.org/issue?@action=redirect&bpo=43317): The `gzip` module's main entry point now sizes its chunks at io.DEFAULT_BUFFER_SIZE. That edges out the older constant of 1024 bytes on speed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
