# What’s New in Python 2.3 / Optimizations

### Optimizations

- Instantiating new-style classes is now considerably quicker; in fact, they outpace classic classes!

- Tim Peters thoroughly rewrote the [`sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method on list objects, and the new implementation runs much faster.

- Multiplying large long integers has become far quicker because of a new implementation of Karatsuba multiplication, whose scaling beats the *O*(*n*2) cost demanded by the familiar grade-school approach to multiplying. (Original patch by Christopher A. Craig, and significantly reworked by Tim Peters.)

- An opcode, `SET_LINENO`, has now been eliminated. Depending on quirks of your compiler, this might yield a modest speedup. Refer to the section Other Changes and Fixes for a fuller discussion. (Removed by Michael Hudson.)

- `xrange()` objects have gained their own iterator, so `for i in xrange(n)` runs a touch faster than `for i in range(n)`. (Patch by Raymond Hettinger.)

- Numerous small reorderings were carried out across various hotspots to boost speed, for instance inlining a function or trimming away a bit of code. (Implemented mostly by GvR, though many other people each contributed an individual change.)

Taken together, the 2.3 optimizations make Python 2.3 finish the pystone benchmark roughly 25% quicker than Python 2.2.

[Subject index](INDEX.md) · [Previous source section](string-changes.md) · [Next source section](standard-library-module-changes.md) · [Release/subject declaration](standard-set-type.md)
