# Constants

# Constants

### Built-in Constants

Just a few constants are defined within the built-in namespace. Here they are:

 False

Represents the falsy member of the [`bool`](https://docs.python.org/3.14/library/functions.html#bool) type. Trying to assign to `False` is not permitted and triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

 True

Represents the truthy member of the [`bool`](https://docs.python.org/3.14/library/functions.html#bool) type. Trying to assign to `True` is not permitted and triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

 None

A value commonly employed to signal that nothing is present, such as when a function call omits its default arguments. Trying to assign to `None` is not permitted and triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). `None` is the sole instance of the [`NoneType`](https://docs.python.org/3.14/library/types.html#types.NoneType) type.

 NotImplemented

A distinctive value that the binary special methods ought to hand back (for instance [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__), [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__), [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__), [`__rsub__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rsub__), and so on) to signal that the operation has no implementation against the other operand's type; the in-place binary special methods (for instance [`__imul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__imul__), [`__iand__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iand__), and so on) may hand it back to serve the same end. Evaluating it within a boolean context is not appropriate. The lone instance of the [`types.NotImplementedType`](https://docs.python.org/3.14/library/types.html#types.NotImplementedType) type is `NotImplemented`.

Note

Should a binary (or in-place) method give back `NotImplemented`, the interpreter then attempts the reflected operation against the other operand's type (or falls back some other way, according to the operator involved). When every such attempt yields `NotImplemented`, the interpreter goes on to raise a fitting exception. Returning `NotImplemented` by mistake produces either a confusing error message or leaks the `NotImplemented` value back out into Python code.

For worked examples, refer to [Implementing the arithmetic operations](https://docs.python.org/3.14/library/numbers.html#implementing-the-arithmetic-operations).

Caution

Do not treat `NotImplemented` and `NotImplementedError` as equivalent. Restrict this constant to the usage outlined above; for guidance on using the exception properly, consult [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Changed in version 3.9: Treating `NotImplemented` as a boolean became deprecated.

Changed in version 3.14: Treating `NotImplemented` as a boolean now triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Earlier it yielded `True` while issuing a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning), behavior that had held since Python 3.9.

 Ellipsis

Identical to the ellipsis literal “`...`”; a value often used as a marker that some portion has been left out. Although you can assign to `Ellipsis`, assigning to `...` instead triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). The single instance of the [`types.EllipsisType`](https://docs.python.org/3.14/library/types.html#types.EllipsisType) type is `Ellipsis`.

 __debug__

When Python is launched without the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) option, this constant holds true. Refer as well to the [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement.

Note

You cannot rebind the names `None`, `False`, `True` and `__debug__` (any assignment to them, even where used as an attribute name, will raise [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError)), which lets them count as genuinely “true” constants.

### Constants added by the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module

The [`site`](https://docs.python.org/3.14/library/site.html#module-site) module — loaded automatically at startup unless the [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) command-line option is supplied — contributes a handful of constants to the built-in namespace. These serve the interactive interpreter shell and ought not appear inside actual programs.

 quit(*code=None*)

 exit(*code=None*)

Objects that, on being printed, emit a message such as “Use quit() or Ctrl-D (i.e. EOF) to exit”; when referenced bare inside the interactive interpreter or invoked as functions, they raise [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) carrying the exit code you provide.

 help

When printed, this object emits “Type help() for interactive help, or help(object) for help about object.” as its output; referencing it bare within the interactive interpreter launches the built-in help system (refer to [`help()`](https://docs.python.org/3.14/library/functions.html#help)).

 copyright

 credits

Objects that, whether printed or invoked, output the copyright text or the credits text, respectively.

 license

An object that, on being printed, shows the message “Type license() to see the full license text”; calling it presents the entire license text page by page, in pager fashion (one screen at a time).

[Subject index](INDEX.md)
