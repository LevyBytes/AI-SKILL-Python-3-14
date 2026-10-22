# Registry Handle Objects

### Registry Handle Objects

This object encloses a Windows HKEY object and shuts it automatically when the object is destroyed. For guaranteed cleanup, invoke either the object's `Close()` method or the `CloseKey()` function.

Every registry function within this module hands back one of these objects.

Every registry function within this module that takes a handle object will also take an integer; even so, using the handle object is the recommended choice.

Handle objects provide semantics for [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__) ? thus

```python
if handle:
    print("Yes")

```

prints `Yes` whenever the handle remains valid at the moment (it hasn't yet been closed or detached).

A handle object may be turned into an integer (for instance, by way of the built-in [`int()`](https://docs.python.org/3.14/library/functions.html#int) function); when that happens, the underlying Windows handle value comes back. The `Detach()` method is another option for getting the integer handle while also severing the Windows handle from the handle object.

 PyHKEY.Close()

Closes the underlying Windows handle.

If the handle is already closed, no error is raised.

 PyHKEY.Detach()

Detaches the Windows handle from the handle object.

What comes back is an integer carrying the handle's value as it stood prior to detachment. When the handle has already been detached or closed, the return is zero.

Once you have called this function, the handle is essentially invalidated, though it is not closed. Reach for this function in cases where the underlying Win32 handle has to outlive the handle object itself.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.PyHKEY.Detach` with argument `key`.

 PyHKEY.__enter__()

 PyHKEY.__exit__(**exc_info*)

Because the HKEY object provides [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) along with [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__), it honors the context protocol used by the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement:

```python
with OpenKey(HKEY_LOCAL_MACHINE, "foo") as key:
    ...  # work with key

```

will automatically close *key* when control leaves the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block.

[Subject index](INDEX.md) · [Previous](winreg-reg-binary-to-winreg-reg-sz.md)
