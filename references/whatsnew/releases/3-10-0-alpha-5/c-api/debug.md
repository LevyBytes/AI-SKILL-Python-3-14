# Python 3.10.0 alpha 5 / c api / debug

[bpo-42979](https://bugs.python.org/issue?@action=redirect&bpo=42979): With Python built in debug mode (carrying C assertions), invoking a type slot such as `sq_length` (`__len__()` in Python) now ends in a fatal error if that slot returned success yet left an exception set, or returned failure with no exception set. The message spells out the slot, the type name, and whatever exception is set (when one is). Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
