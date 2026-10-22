# generator.throw(*value*) / generator.throw(*type*[, *value*[, *traceback*]])

generator.throw(*value*)

 generator.throw(*type*[, *value*[, *traceback*]])

Throws an exception at the spot where the generator had paused, then hands back the generator function's next yielded value. Should the generator finish without producing a further value, it raises a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception. When the generator function neither catches the supplied exception nor raises some other one, that exception travels onward to the caller.

The usual pattern passes one exception instance, in much the same fashion that the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) keyword gets used.

To stay compatible with older code, though, the alternate signature remains available, honoring a convention carried over from earlier Python releases. Here the *type* argument ought to be an exception class, and *value* ought to be an exception instance. When *value* is left out, the *type* constructor runs to obtain an instance. Supplying *traceback* attaches it to the exception; otherwise whatever [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute is already kept in *value* may be wiped.

Changed in version 3.12: The alternate signature (type[, value[, traceback]]) now carries a deprecation and could disappear in some later Python release.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](yield-expressions.md) · [Owning language section](generator-iterator-methods.md) · [Previous source section](generator-send.md) · [Following source section](generator-close.md)
