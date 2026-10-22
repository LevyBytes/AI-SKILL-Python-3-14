# What's New In Python 3.3 / Features

### Features

- Every native single character format specifier from the struct module syntax (which may carry an optional ?@? prefix) is now handled.

- Subject to a few limits, the cast() method permits altering both the format and the shape of C-contiguous arrays.

- Representations that are multi-dimensional now work for arrays of any type.

- Comparisons that are multi-dimensional now work for arrays of any type.

- One-dimensional memoryviews over hashable (read-only) types whose formats are B, b or c can now be hashed. (Contributed by Antoine Pitrou in [bpo-13411](https://bugs.python.org/issue?@action=redirect&bpo=13411).)

- Any 1-D array type now permits arbitrary slicing. As one illustration, you can now reverse a memoryview in *O*(1) by applying a negative step.

[Subject index](INDEX.md) · [Previous source section](pep3118-memoryview-and-buffer-protocol.md) · [Next source section](api-changes.md) · [Release/subject declaration](summary-release-highlights.md)
