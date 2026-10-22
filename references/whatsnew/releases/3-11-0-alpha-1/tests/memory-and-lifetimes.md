# Python 3.11.0 alpha 1 / tests / memory and lifetimes

[bpo-44895](https://bugs.python.org/issue?@action=redirect&bpo=44895): To shrink the chance of a false alarm during reference-leak checks, libregrtest now flushes the type cache at a later point. Formerly the type cache was wiped too soon, and under very particular conditions libregrtest reported a spurious reference leak. Irit Katriel and Victor Stinner authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
