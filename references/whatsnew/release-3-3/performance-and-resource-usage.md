# What's New In Python 3.3 / Performance and resource usage

### Performance and resource usage

How a Unicode string is stored now hinges on the loftiest code point it contains:

- pure ASCII and Latin1 strings (`U+0000-U+00FF`) take up 1 byte for each code point;

- BMP strings (`U+0000-U+FFFF`) take up 2 bytes for each code point;

- non-BMP strings (`U+10000-U+10FFFF`) take up 4 bytes for each code point.

The upshot is that, for the bulk of applications, the memory devoted to string storage should drop markedly ? most of all versus the old wide unicode builds ? because, more often than not, strings turn out to be pure ASCII even in international settings (since plenty of strings carry non-human language data, such as XML fragments, HTTP headers, JSON-encoded data, etc.). For those same reasons, we are likewise hopeful that CPU cache efficiency will rise on non-trivial applications. Measured on a Django benchmark, Python 3.3 uses two to three times less memory than Python 3.2, and edges out Python 2.7 by a small margin (the PEP has the particulars).

See also

[**PEP 393**](https://peps.python.org/pep-0393/) - Flexible String Representation

PEP written by Martin von Löwis; implementation by Torsten Becker and Martin von Löwis.

[Subject index](INDEX.md) · [Previous source section](functionality.md) · [Next source section](pep-397-python-launcher-for-windows.md) · [Release/subject declaration](summary-release-highlights.md)
