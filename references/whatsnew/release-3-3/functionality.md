# What's New In Python 3.3 / Functionality - sys

### Functionality

The changes that [**PEP 393**](https://peps.python.org/pep-0393/) brought in are as follows:

- Python now covers the entire span of Unicode code points at all times, the non-BMP ones included (that is, from `U+0000` to `U+10FFFF`). There is no longer any narrow-versus-wide build split, and Python now acts as a wide build everywhere, Windows included.

- Since narrow builds are gone, the issues that were unique to narrow builds are likewise resolved, for instance:

  - [`len()`](https://docs.python.org/3.14/library/functions.html#len) now consistently gives 1 for non-BMP characters, hence `len('\U0010FFFF') == 1`;

  - string literals no longer recombine surrogate pairs, hence `'\uDBFF\uDFFF' != '\U0010FFFF'`;

  - indexing into or slicing non-BMP characters yields what you expect, hence `'\U0010FFFF'[0]` now produces `'\U0010FFFF'` rather than `'\uDBFF'`;

  - every remaining standard library function now manages non-BMP code points correctly.

- [`sys.maxunicode`](https://docs.python.org/3.14/library/sys.html#sys.maxunicode) now always carries the value `1114111` (`0x10FFFF` in hexadecimal). For backward compatibility the `PyUnicode_GetMax()` function still hands back either `0xFFFF` or `0x10FFFF`, and the new Unicode API should not be paired with it (see [bpo-13054](https://bugs.python.org/issue?@action=redirect&bpo=13054)).

- The `./configure` flag `--with-wide-unicode` is gone.

[Subject index](INDEX.md) · [Previous source section](pep-393-flexible-string-representation.md) · [Next source section](performance-and-resource-usage.md) · [Release/subject declaration](summary-release-highlights.md)
