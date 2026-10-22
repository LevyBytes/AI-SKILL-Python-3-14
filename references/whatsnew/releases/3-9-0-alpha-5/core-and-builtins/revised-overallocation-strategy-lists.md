# Python 3.9.0 alpha 5 / core and builtins / revised overallocation strategy lists

[bpo-38373](https://bugs.python.org/issue?@action=redirect&bpo=38373): Revised the overallocation strategy for lists. Overallocation is now skipped when the new size sits nearer to the overallocated size than to the old size and pads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
