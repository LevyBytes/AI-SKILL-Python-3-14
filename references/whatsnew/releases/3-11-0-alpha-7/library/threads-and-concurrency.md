# Python 3.11.0 alpha 7 / library / threads and concurrency

[bpo-42369](https://bugs.python.org/issue?@action=redirect&bpo=42369): Make `zipfile._SharedFile.tell()` thread-safe so that reading a `ZipFile` across several threads no longer triggers a “zipfile.BadZipFile: Bad CRC-32 for file” exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
