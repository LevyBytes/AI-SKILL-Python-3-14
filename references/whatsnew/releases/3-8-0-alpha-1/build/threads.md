# Python 3.8.0 alpha 1 / build / threads

[bpo-33015](https://bugs.python.org/issue?@action=redirect&bpo=33015): Repair an undefined behaviour inside the pthread version of [`PyThread_start_new_thread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThread_start_new_thread): introduce a function wrapper that consistently returns `NULL`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
