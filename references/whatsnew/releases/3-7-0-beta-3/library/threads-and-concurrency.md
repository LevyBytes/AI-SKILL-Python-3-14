# Python 3.7.0 beta 3 / library / threads and concurrency

[bpo-33021](https://bugs.python.org/issue?@action=redirect&bpo=33021): Release the GIL across fstat() calls, which avoids hanging every thread when mmap.mmap(), os.urandom(), and random.seed() run. Patch by Nir Soffer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
