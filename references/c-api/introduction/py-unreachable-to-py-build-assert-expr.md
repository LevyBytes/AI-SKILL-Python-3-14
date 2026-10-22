# Assertion utilities

#### Assertion utilities

 Py_UNREACHABLE()

Reach for this wherever you have a code path that, by design, can never actually be hit. One example is the `default:` clause within a `switch` statement whose `case` statements already cover every possible value. Put it wherever the temptation would be to drop in an `assert(0)` or `abort()` call.

Within release mode, this macro lets the compiler tune the code and sidesteps any unreachable-code warning. On GCC in release mode, for instance, the macro is built atop `__builtin_unreachable()`.

Within debug mode, as well as on compilers that don't support it, the macro expands into a call to [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError).

One occasion for `Py_UNREACHABLE()` is right after calling a function that never comes back yet isn't marked `_Noreturn`.

When a code path is highly improbable yet still reachable in some exceptional situation, steer away from this macro. Examples include a low memory condition or a system call handing back a value beyond the anticipated range. In such a case, reporting the error back to the caller is the better move. Where you can't surface the error to the caller, [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError) is available.

Added in version 3.7.

 Py_SAFE_DOWNCAST(value, larger, smaller)

Casts *value* from type *larger* down to type *smaller*, while confirming that nothing was lost.

In release builds of Python, this comes close to `((*smaller*) *value*)` (under C++, `static_cast<*smaller*>(*value*)` gets used in its place).

In debug builds (which implies `Py_DEBUG` has been defined), it asserts that the cast from *larger* down to *smaller* lost nothing.

Since *value*, *larger*, and *smaller* may each be evaluated several times within the expression, never hand this macro an expression carrying side-effects directly.

 Py_BUILD_ASSERT(cond)

Asserts the compile-time condition *cond* as a statement. Should the condition prove false or prove impossible to evaluate at compile time, the build fails.

Roughly equivalent to `static_assert(*cond*)` from C23 onward.

For example:

```c
Py_BUILD_ASSERT(sizeof(PyTime_t) == sizeof(int64_t));

```

Added in version 3.3.

 Py_BUILD_ASSERT_EXPR(cond)

Asserts the compile-time condition *cond* as an expression whose value is `0`. Should the condition prove false or prove impossible to evaluate at compile time, the build fails.

For example:

```c
#define foo_to_char(foo) \
    ((char *)(foo) + Py_BUILD_ASSERT_EXPR(offsetof(struct foo, string) == 0))

```

Added in version 3.3.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-unused-to-py-gcc-attribute.md) · [Previous source contract](py-abs-to-py-charmask.md) · [Following source contract](py-array-length-to-py-member-size.md)
