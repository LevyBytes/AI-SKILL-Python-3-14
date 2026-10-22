# What’s New in Python 2.2 / PEP 238: Changing the Division Operator

### PEP 238: Changing the Division Operator

Python 2.2's most divisive alteration marks the opening move in a campaign to repair a long-standing design flaw present since Python's earliest days. As things stand, Python’s division operator, `/`, mimics C’s division operator once it sees two integer arguments: it yields an integer result, chopped downward whenever a fractional part would appear. Take `3/2`, which gives 1 rather than 1.5, and `(-1)/2`, which gives -1 rather than -0.5. The upshot is that a division’s outcome can shift surprisingly with the types of the two operands, and since Python types things dynamically, pinning down which types the operands might be is often hard.

(What's disputed is whether this counts as a *real* design flaw at all, and whether fixing it justifies breaking code already out there. The matter set off interminable threads on python-dev and, come July 2001, blew up into a flurry of bitingly sarcastic posts across *comp.lang.python*. I'll take neither position here and confine myself to laying out what 2.2 actually ships. See [**PEP 238**](https://peps.python.org/pep-0238/) for a roundup of the points raised on both sides.)

Given that this change has the potential to break code, it is being phased in with great care. The transition opens with Python 2.2, yet the changeover stays unfinished right up until Python 3.0.

To begin, let me lift a bit of vocabulary from [**PEP 238**](https://peps.python.org/pep-0238/). “True division” names the division most people outside programming already know: 3/2 is 1.5, 1/4 is 0.25, and onward. “Floor division” describes what Python’s `/` operator does today with integer operands; you get the floor of whatever true division would have returned. “Classic division” refers to the present hybrid conduct of `/`; it hands back floor division’s result for integer operands and true division’s result whenever one operand is a floating-point number.

Here are the changes 2.2 introduces:

- There's a new operator, `//`, the floor division operator. (Indeed, we're aware it resembles C++'s comment marker.) Regardless of its operands' types, `//` *always* carries out floor division, so `1 // 2` is 0 while `1.0 // 2.0` comes out as 0.0.

`//` ships ready to use in Python 2.2; no `__future__` statement is required to enable it.

- Drop a `from __future__ import division` into a module and the `/` operator switches to handing back true division's result, so `1/2` becomes 0.5. Leave that `__future__` statement out and `/` keeps meaning classic division. What `/` means by default holds steady until Python 3.0.

- A class may supply methods named [`__truediv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__truediv__) and [`__floordiv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__floordiv__) to override the pair of division operators. Down at the C level, the [`PyNumberMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods) structure carries slots too, letting extension types implement both operators.

- Python 2.2 ships a handful of command-line arguments that let you check whether code holds up under the revised division behaviour. Launch python with `-Q warn` and every time division gets applied to two integers a warning fires. That lets you track down code the change touches and repair it. Out of the box, Python 2.2 just does classic division silently; the warning gets switched on by default starting in Python 2.3.

See also

[**PEP 238**](https://peps.python.org/pep-0238/) - Changing the Division Operator

Authored by Moshe Zadka and Guido van Rossum. The implementation was done by Guido van Rossum..

[Subject index](INDEX.md) · [Previous source section](pep-237-unifying-long-integers-and-integers.md) · [Next source section](unicode-changes.md) · [Release/subject declaration](introduction.md)
