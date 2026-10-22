# exceptions: `ExceptionGroup`, `BaseExceptionGroup`, `subgroup()`, `split()`

### Exception groups

The classes below come into play when several unrelated exceptions must be raised together. Being part of the exception hierarchy, they can be caught with [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) just like any other exception. On top of that, [`except*`](https://docs.python.org/3.14/reference/compound_stmts.html#except-star) recognizes them, matching their subgroups by the types of the exceptions they hold.

 *exception *ExceptionGroup(*msg*, *excs*)

 *exception *BaseExceptionGroup(*msg*, *excs*)

Each of these exception types bundles the exceptions found in the sequence `excs`. The `msg` parameter has to be a string. What sets the two classes apart is that `BaseExceptionGroup` derives from `BaseException` and can bundle any exception, whereas `ExceptionGroup` derives from `Exception` and can bundle only subclasses of `Exception`. The point of this arrangement is that `except Exception` catches an `ExceptionGroup` yet not a `BaseExceptionGroup`.

When every contained exception is an `Exception` instance, the `BaseExceptionGroup` constructor returns an `ExceptionGroup` instead of a `BaseExceptionGroup`, so it can drive the choice for you automatically. The `ExceptionGroup` constructor, by contrast, throws a `TypeError` should any contained exception fail to be an `Exception` subclass.

Over the type of the exceptions they contain, exception groups are [generic](https://docs.python.org/3.14/library/typing.html#generics).

**CPython implementation detail:** Although the `excs` parameter accepts any sequence, lists and tuples in particular are handled more efficiently here. To get the best performance, pass a tuple as `excs`.

 message

The `msg` argument handed to the constructor. This attribute is read-only.

 exceptions

A tuple holding the exceptions from the `excs` sequence supplied to the constructor. This attribute is read-only.

 subgroup(*condition*)

Returns an exception group holding only those exceptions from the current group that satisfy *condition*, or `None` when nothing qualifies.

The condition may be an exception type or a tuple of exception types, in which case each exception is tested for a match by the same check an `except` clause applies. The condition may instead be a callable (other than a type object) that takes an exception as its lone argument and returns true for the exceptions belonging in the subgroup.

The result keeps the current exception’s nesting structure intact, along with the values of its `message`, `__traceback__`, `__cause__`, `__context__` and `__notes__` fields. Nested groups that end up empty are dropped from the result.

The condition is evaluated against every exception in the nested exception group, the top-level one and any nested exception groups included. Where the condition holds for such an exception group, that group goes into the result whole.

Added in version 3.13: so long as it is not a type object, `condition` may now be any callable.

 split(*condition*)

Behaves like `subgroup()`, except it returns the pair `(match, rest)` in which `match` equals `subgroup(condition)` and `rest` is the leftover non-matching portion.

[Subject index](INDEX.md) · [Previous](warning-to-resourcewarning.md) · [Continue](derive.md)
