# Python 3.9.0 alpha 6 / library / collections and iteration

[bpo-40325](https://bugs.python.org/issue?@action=redirect&bpo=40325): Handling of set objects within random.sample() is now deprecated.

[bpo-40014](https://bugs.python.org/issue?@action=redirect&bpo=40014): Repair `os.getgrouplist()`: should the `getgrouplist()` call fail due to an undersized group list, the attempt is repeated with a bigger one. When it fails, glibc's `getgrouplist()` writes the full group count into `ngroups`. Elsewhere, the group list size is simply doubled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
