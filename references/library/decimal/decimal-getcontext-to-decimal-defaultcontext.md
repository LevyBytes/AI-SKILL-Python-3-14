# decimal: `decimal.getcontext()`, `decimal.setcontext()`, `decimal.localcontext()`, `decimal.IEEEContext()`, `decimal.BasicContext`, `decimal.ExtendedContext`, `decimal.DefaultContext`

### Context objects

Contexts act as environments for arithmetic operations. They control precision, fix the rules for rounding, decide which signals get handled as exceptions, and constrain the range of exponents.

Every thread keeps its own current context, reached or altered through the `getcontext()` and `setcontext()` functions:

 decimal.getcontext()

Yield the current context belonging to the active thread.

 decimal.setcontext(*c*, */*)

Assign *c* as the current context of the active thread.

You may also rely on the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement together with the `localcontext()` function to switch the active context for a time.

 decimal.localcontext(*ctx=None*, ***kwargs*)

Yield a context manager that, on entry to the with-statement, makes the active thread's current context a copy of *ctx*, then reinstates the prior context once the with-statement ends. Absent a supplied context, a copy of the current context serves instead. The *kwargs* argument configures the attributes of the freshly made context.

To illustrate, the following code raises the current decimal precision to 42 places, runs a calculation, and afterward restores the prior context on its own:

```python
from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 42   # Perform a high precision calculation
    s = calculate_something()
s = +s  # Round the final result back to the default precision

```

Written with keyword arguments, the code would read as follows:

```python
from decimal import localcontext

with localcontext(prec=42) as ctx:
    s = calculate_something()
s = +s

```

Raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when *kwargs* names an attribute that `Context` does not support. Raises either `TypeError` or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *kwargs* assigns an invalid value to an attribute.

Changed in version 3.11: `localcontext()` can now assign context attributes when you pass them as keyword arguments.

 decimal.IEEEContext(*bits*)

Yield a context object set up with the right values for one of the IEEE interchange formats. The argument has to be a multiple of 32 and below `IEEE_CONTEXT_MAX_BITS`.

Added in version 3.14.

Fresh contexts may likewise be built with the `Context` constructor covered below. On top of that, the module ships three ready-made contexts:

 decimal.BasicContext

A standard context laid out by the General Decimal Arithmetic Specification. Precision sits at nine. Rounding sits at `ROUND_HALF_UP`. Every flag starts cleared. Every trap is enabled (handled as exceptions) apart from `Inexact`, `Rounded`, and `Subnormal`.

Since so many of its traps are enabled, this context comes in handy for debugging.

 decimal.ExtendedContext

A standard context laid out by the General Decimal Arithmetic Specification. Precision sits at nine. Rounding sits at `ROUND_HALF_EVEN`. Every flag starts cleared. No trap is enabled (so that computations never raise exceptions).

Since its traps stay disabled, this context suits applications that would rather end up with a result value of `NaN` or `Infinity` than raise exceptions. That lets an application finish a run despite conditions that would otherwise stop the program.

 decimal.DefaultContext

The `Context` constructor draws on this context as a prototype for new contexts. Altering a field (precision, say) shifts the default applied to new contexts that the `Context` constructor builds.

This context proves most valuable in multi-threaded environments. Altering one of its fields before any threads start sets system-wide defaults. Altering the fields once threads are running is discouraged, since doing so would demand thread synchronization to avoid race conditions.

Within single threaded environments, skipping this context entirely is the better choice. Just build contexts explicitly, as described below.

The defaults are `Context.prec`=`28`, `Context.rounding`=`ROUND_HALF_EVEN`, plus enabled traps for `Overflow`, `InvalidOperation`, and `DivisionByZero`.

Beyond the three contexts that ship, fresh contexts can be built with the `Context` constructor.

[Subject index](INDEX.md) · [Previous](logical-operands.md) · [Continue](decimal-context-class-to-decimal-context-create-decimal.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)
