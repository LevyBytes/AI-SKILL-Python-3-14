# selectors / Classes: `selectors.BaseSelector`, `modify()`, `close()`, `get_key()`

*class *selectors.BaseSelector

You lean on a `BaseSelector` when you need to await I/O event readiness over many file objects together. It allows registering and unregistering file streams, plus a method that awaits I/O events across those streams under an optional timeout. Being an abstract base class, it can never be instantiated directly. Turn to `DefaultSelector` in its place, or grab one of `SelectSelector`, `KqueueSelector` etc. should you wish to nail down a particular build that your platform can support. Both `BaseSelector` and the concrete builds derived from it honor the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol.

 *abstractmethod *register(*fileobj*, *events*, *data=None*)

Sign up a file object for selection, keeping watch over it for I/O events.

*fileobj* names the file object you want watched. It can come as either an integer file descriptor or an object that carries a `fileno()` method. *events* is a bitwise mask spelling out which events to watch. *data* is simply an opaque object.

Back comes a fresh `SelectorKey` instance; failing that, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised whenever the event mask or file descriptor is bad, or a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) when the file object already has a registration.

 *abstractmethod *unregister(*fileobj*)

Drop a file object from selection, taking it out of the watch set. Any file object ought to be dropped this way before you close it.

*fileobj* has to name a file object that was registered at some earlier point.

What comes back is the matching `SelectorKey` instance; otherwise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when *fileobj* lacks a registration. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) follows when *fileobj* is bad (for instance it carries no `fileno()` method, or its `fileno()` method yields an invalid return value).

 modify(*fileobj*, *events*, *data=None*)

Alter the watched events, or the data hung off, for a file object that is already registered.

In effect this matches a `BaseSelector.unregister(fileobj)` call trailed by `BaseSelector.register(fileobj, events, data)`, the difference being that it admits a more efficient implementation.

Back comes a fresh `SelectorKey` instance; otherwise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised should the event mask or file descriptor be bad, or a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) should the file object hold no registration.

 *abstractmethod *select(*timeout=None*)

Block until one or more registered file objects turn ready, or until the timeout runs out.

Where `timeout > 0`, the value caps how long the wait may last, measured in seconds. Where `timeout <= 0`, the call returns at once without blocking and tells you which file objects are ready right then. Where *timeout* equals `None`, the call holds until one of the watched file objects turns ready.

What you get back is a list holding one `(key, events)` tuple per ready file object.

*key* names the `SelectorKey` instance that lines up with a ready file object. *events* is a bitmask covering the events now ready on that file object.

Note

Should the running process catch a signal, this method may hand back control even though no file object has turned ready and the timeout still has time left; under that circumstance you get an empty list.

Changed in version 3.5: Where a signal cuts in and the signal handler raised nothing, the selector now retries with its timeout recalculated (the reasoning sits in [**PEP 475**](https://peps.python.org/pep-0475/)), rather than handing back an empty event list ahead of the timeout.

 close()

Close the selector.

Calling this is what guarantees every backing resource gets released. Once a selector has been closed, you must not keep using it.

 get_key(*fileobj*)

Hand back the key tied to a file object that is registered.

Back comes the `SelectorKey` instance bound to this file object; failing that, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when the file object holds no registration.

 *abstractmethod *get_map()

Hand back a mapping that links file objects across to their selector keys.

What you get is a [`Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) instance that pairs each registered file object with the `SelectorKey` instance bound to it.

[Subject index](INDEX.md) · [Previous](classes.md) · [Continue](selectors-defaultselector-class.md) · [Owning module, declaration or section: selectors](selectors-high-level-i-o-multiplexing.md) · [Owning module, declaration or section: Classes](selectors-selectorkey-class.md)
