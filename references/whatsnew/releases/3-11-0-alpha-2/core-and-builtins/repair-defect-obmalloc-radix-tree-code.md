# Python 3.11.0 alpha 2 / core and builtins / repair defect obmalloc radix tree code

[bpo-45521](https://bugs.python.org/issue?@action=redirect&bpo=45521): Repair a defect in the obmalloc radix tree code. On 64-bit hardware, the defect makes the tree carry 46-bits of virtual addresses rather than the 48-bits that were intended.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
