# sys.unraisablehook

sys.unraisablehook(*unraisable*, */*)

Deals with an unraisable exception.

Invoked once an exception has come up that Python has no way to deal with — say, when a destructor throws, or in the course of garbage collection ([`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect)).

These are the attributes carried by the *unraisable* argument:

- `exc_type`: the type of the exception.

- `exc_value`: the exception’s value, which may be `None`.

- `exc_traceback`: the exception’s traceback, which may be `None`.

- `err_msg`: the error message, which may be `None`.

- `object`: the object behind the exception, which may be `None`.

The built-in hook renders `err_msg` and `object` as `f'{err_msg}: {object!r}'`, falling back to the “Exception ignored in” error message whenever `err_msg` is `None`.

You may override `sys.unraisablehook()` to steer how unraisable exceptions get dealt with.

See also

`excepthook()`, which deals with exceptions that go uncaught.

Warning

Holding onto `exc_value` from within a custom hook can spawn a reference cycle. Clear it outright to sever that cycle once you no longer need the exception.

Holding onto `object` from within a custom hook can bring it back to life if it points at an object midway through finalization. Steer clear of retaining `object` past the point the custom hook returns, so objects don’t get resurrected.

Fires an auditing event `sys.unraisablehook` carrying the arguments *hook*, *unraisable* whenever an exception that can’t be handled crops up. That *unraisable* object matches the one destined for the hook. With no hook set, *hook* may be `None`.

Added in version 3.8.

[API family](INDEX.md) · [sys context index](../INDEX.md).
