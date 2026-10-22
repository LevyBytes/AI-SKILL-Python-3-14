# Python 3.5.0 alpha 1 / library / ctypes

[bpo-22176](https://bugs.python.org/issue?@action=redirect&bpo=22176): The libffi bundled with the ctypes module was bumped to v3.1. With this release come the Linux AArch64 and POWERPC ELF ABIv2 little endian architectures.

[bpo-10744](https://bugs.python.org/issue?@action=redirect&bpo=10744): [**PEP 3118**](https://peps.python.org/pep-3118/) format strings on ctypes objects that have a nontrivial shape were fixed.

[bpo-22098](https://bugs.python.org/issue?@action=redirect&bpo=22098): Both BigEndianStructure and LittleEndianStructure in ctypes now declare an empty __slots__, sparing subclasses from automatically acquiring a per-instance dict. Claudiu Popa wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
