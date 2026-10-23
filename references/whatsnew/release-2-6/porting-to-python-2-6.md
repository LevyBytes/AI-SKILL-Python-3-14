# What’s New in Python 2.6 / Porting to Python 2.6 - collections, datetime, socket, xmlrpc.client

### Porting to Python 2.6

Gathered here are the already-mentioned changes plus further bug fixes that might force you to adjust your code:

- A class meant to be unhashable ought to declare `__hash__ = None` within its body to signal as much.

- Exceptions made of strings are gone now. Try to use one and you get a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

- On [`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque), the `__init__()` method wipes whatever the deque already holds before it pulls in the iterable's elements. With that, its behavior now lines up with `list.__init__()`.

- In earlier releases, [`object.__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) would take whatever positional and keyword arguments you threw at it and quietly discard them. Python 2.6 forbids that and hands back a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) instead. The fallout lands on any `__init__()` that winds up invoking the matching method on [`object`](https://docs.python.org/3.14/library/functions.html#object) — say, by way of [`super()`](https://docs.python.org/3.14/library/functions.html#super). The discussion lives at [bpo-1683368](https://bugs.python.org/issue?@action=redirect&bpo=1683368).

- Hand the `Decimal` constructor a string padded with whitespace at either end and it now tolerates it, where before it would throw an `InvalidOperation` exception. The reverse holds for the `create_decimal()` method on `Context` objects, which now flatly rejects any stray whitespace and throws a `ConversionSyntax` exception.

- By a quirk of how it was built, the built-in [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function used to go ahead and import a file when you handed it a file path. That was never the intent, so the code now watches for exactly that situation and throws an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError).

- C API: out of the box, the [`PyImport_Import()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_Import) and [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) functions now reach for absolute imports rather than relative ones. C extensions that pull in other modules will feel this.

- C API: an extension data type that ought not be hashable should point its `tp_hash` slot at [`PyObject_HashNotImplemented()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HashNotImplemented).

- Within the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module, the [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error) exception now descends from [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError). It formerly sat outside `StandardError`, but by way of `IOError` it now falls under it. (Implemented by Gregory P. Smith; [bpo-1706815](https://bugs.python.org/issue?@action=redirect&bpo=1706815).)

- The [`xmlrpclib`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) module has stopped silently turning [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) into the [`xmlrpclib.DateTime`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.DateTime) type, since that conversion did not hold up correctly for every application. Anything leaning on `xmlrpclib` ought to convert its `date` and `time` instances itself. ([bpo-1330538](https://bugs.python.org/issue?@action=redirect&bpo=1330538))

- (3.0-warning mode) Reaching into the [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) class through a slice or an index now produces a warning; letting `Exception` act like a tuple is on its way out.

- (3.0-warning mode) Putting two dictionaries, or two objects lacking comparison methods, through an inequality check now surfaces a warning. `dict1 == dict2` carries on working, yet `dict1 < dict2` is on its way out.

Stacking one cell against another — cells being a behind-the-scenes piece of how Python handles scoping — likewise draws a warning, given that 3.0 bans such comparisons outright.

When your application embeds Python:

- Python 2.6.6 introduced the `PySys_SetArgvEx()` function so applications could seal a security hole that came with relying on the older `PySys_SetArgv()`. Look at whether your code invokes `PySys_SetArgv()`, and weigh carefully whether it ought to switch to `PySys_SetArgvEx()` with *updatepath* set to false.

[Subject index](INDEX.md) · [Previous source section](port-specific-changes-irix.md) · [Release/subject declaration](python-3-0.md)
