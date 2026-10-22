# urllib.request: `BaseHandler.add_parent()`, `BaseHandler.close()`, `BaseHandler.parent`, `BaseHandler.default_open()`, `BaseHandler.unknown_open()`

### BaseHandler Objects

`BaseHandler` objects supply a handful of methods that are useful on their own, plus others designed to be called by subclasses. The ones meant for direct use are:

 BaseHandler.add_parent(*director*)

Add a director as parent.

 BaseHandler.close()

Remove any parents.

Only classes that derive from `BaseHandler` ought to make use of the attribute and methods that follow.

Note

By convention, any subclass that defines `<protocol>_request()` or `<protocol>_response()` methods carries a `*Processor` name, while every other subclass carries a `*Handler` name.

 BaseHandler.parent

A valid `OpenerDirector`; you can lean on it to open by way of another protocol, or to deal with errors.

 BaseHandler.default_open(*req*)

`BaseHandler` does *not* define this method, though subclasses ought to define it when they wish to catch every URL.

Whenever it is implemented, the parent `OpenerDirector` invokes this method. It ought to give back a file-like object of the sort described for the return value of `OpenerDirector`'s `open()` method, or else `None`. It ought to raise [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError), barring a genuinely exceptional occurrence (for instance, [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) ought not be turned into `URLError`).

This method will be called before any protocol-specific open method.

 BaseHandler.&lt;protocol&gt;_open(req)

`BaseHandler` does *not* define this method, though subclasses ought to define it when they wish to handle URLs carrying the given protocol.

Whenever it is defined, the parent `OpenerDirector` invokes this method. The values it returns ought to match those for `default_open()`.

 BaseHandler.unknown_open(*req*)

`BaseHandler` does *not* define this method, though subclasses ought to define it when they wish to catch every URL that has no specifically registered handler to open it.

Whenever it is implemented, the `parent` `OpenerDirector` invokes this method. The values it returns ought to match those for `default_open()`.

[Subject index](INDEX.md) · [Previous](openerdirector-add-handler-to-openerdirector-error.md) · [Continue](basehandler-http-error-default.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
