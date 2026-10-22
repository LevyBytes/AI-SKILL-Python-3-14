# Python 3.10.0 alpha 3 / build / threads and concurrency

[bpo-42398](https://bugs.python.org/issue?@action=redirect&bpo=42398): Resolve a race condition in ?make regen-all? that surfaced when make -jN is used to run jobs in parallel. The clinic.py script now writes files only via atomic write. On top of that, generated files stay untouched when their content has not changed, leaving the file modification time alone.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
