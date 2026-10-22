# What's New In Python 3.3 / PEP 393: Flexible String Representation

### PEP 393: Flexible String Representation

The Unicode string type has been altered so that its internal layout can vary, chosen by the largest Unicode ordinal among the characters in the string (taking 1, 2, or 4 bytes). That yields a storage-thrifty form in the usual cases while still granting full UCS-4 on every system. To keep existing APIs working, several representations can coexist; that compatibility layer is expected to be retired as time goes on.

From the Python perspective, this change brings no drawback.

From the C API perspective, [**PEP 393**](https://peps.python.org/pep-0393/) preserves complete backward compatibility. The legacy API ought to stay available for no less than five years. Code relying on the legacy API won't reap the full memory savings, and may even ? worse still ? consume slightly more memory, since Python may need to keep two copies of each string (one in the legacy format and one in the new efficient storage).

[Subject index](INDEX.md) · [Previous source section](api-changes.md) · [Next source section](functionality.md) · [Release/subject declaration](summary-release-highlights.md)
