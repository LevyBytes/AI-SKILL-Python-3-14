# Python 3.13.0 alpha 1 / core and builtins / drop last two codeunit superinstructions

[gh-105229](https://github.com/python/cpython/issues/105229): Drop the last two-codeunit superinstructions. Every superinstruction that survives now occupies just one codeunit, which eases instrumentation along with quickening.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
