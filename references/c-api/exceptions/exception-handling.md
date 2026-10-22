# Exception Handling

### Exception Handling

This chapter's functions give you the means to raise and handle Python exceptions. A grasp of the fundamentals of Python's exception model is essential. The mechanism resembles the POSIX `errno` variable somewhat: a per-thread global flag records whichever error happened most recently. On success, the bulk of C API functions leave this flag untouched, yet on failure they set it to signal what went wrong. Likewise, most C API functions hand back an error indicator too, typically `NULL` when a pointer is expected, or `-1` for an integer return (the exception being the `PyArg_*` functions, which yield `1` on success and `0` on failure).

In concrete terms, three object pointers make up the error indicator: the type of the exception, its value, and the traceback object. When unset, any of these pointers may be `NULL` (though certain pairings are not allowed — for instance, a non-`NULL` traceback paired with a `NULL` exception type is illegal).

Should a function need to fail because a function it invoked failed, it usually leaves the error indicator alone; the called function has already set it. The function's duty is then to either deal with the error and clear the exception, or to return after releasing whatever resources it owns (object references or memory allocations, say); it must *not* keep running normally unless it is ready to cope with the error. When returning on account of an error, signaling to the caller that an error has been set is essential. Should the error go unhandled or be propagated without care, later calls into the Python/C API can misbehave and fail in baffling ways.

Note

The error indicator is **not** the same as the result of [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info). The former stands for an exception that has yet to be caught (so it is still propagating), whereas the latter hands back an exception once it has been caught (so propagation has stopped).

[Subject index](INDEX.md) · [Following source contract](pyerr-clear-to-pyerr-displayexception.md)
