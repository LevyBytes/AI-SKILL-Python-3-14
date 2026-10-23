# What's New In Python 3.4 / PEP 456: Secure and Interchangeable Hash Algorithm - sys

### PEP 456: Secure and Interchangeable Hash Algorithm

[**PEP 456**](https://peps.python.org/pep-0456/) builds on prior security-hardening efforts targeting Python's hash algorithm, tackling some DOS attacks that can hit public-facing APIs which rely on dictionary lookups underneath. (Refer to [bpo-14621](https://bugs.python.org/issue?@action=redirect&bpo=14621) for where this latest wave of improvements began.) This PEP consolidates CPython's hash code so a packager can drop in an alternative hash algorithm more easily, and flips Python's stock implementation over to a SipHash one wherever a 64-bit data type exists. Whatever speed gap shows up against the previous FNV algorithm stays negligible.

The PEP appends extra fields onto the [`sys.hash_info`](https://docs.python.org/3.14/library/sys.html#sys.hash_info) named tuple so they document the hash algorithm the running binary currently relies on. Beyond that, the PEP leaves every existing CPython API untouched.

[Subject index](INDEX.md) · [Previous source section](pep-442-safe-object-finalization.md) · [Next source section](pep-436-argument-clinic.md) · [Release/subject declaration](release-highlights.md)
