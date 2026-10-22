# What's New In Python 3.7 / Module Removals

### Module Removals

The `fpectl` module has been taken out. Never switched on by default, it never operated correctly on x86-64, and its alterations to the Python ABI led to surprising breakage among C extensions. (Contributed by Nathaniel J. Smith in [bpo-29137](https://bugs.python.org/issue?@action=redirect&bpo=29137).)

[Subject index](INDEX.md) · [Previous source section](api-and-feature-removals.md) · [Next source section](windows-only-changes.md) · [Release/subject declaration](summary-release-highlights.md)
