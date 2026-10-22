# Python 3.12.0 alpha 7 / core and builtins / numbers

[gh-101291](https://github.com/python/cpython/issues/101291): Reshuffle the bits within the first field (the one after the header) of PyLongObject. * Bits 0 and 1: 1 - sign. That is, 0 marks positive numbers, 1 marks zero, and 2 marks negative numbers. * Bit 2 held in reserve (likely for the immortal bit) * Bits 3 onward carry the unsigned size.

A handful of operations get a touch more efficient this way, and it opens the door to a tighter, quicker 2s-complement encoding for most ints down the road.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
