# Language and standard library pending removal in 3.14: argparse; ast; asyncio; email; importlib.abc deprecated classes

## Pending removal in Python 3.14

### Pending removal in Python 3.14

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse): On `argparse.BooleanOptionalAction`, the *type*, *choices*, and *metavar* parameters are deprecated, with removal targeted for 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248).)

- [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast): Documentation has flagged the items below as deprecated since Python 3.8; they now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) at runtime whenever accessed or used, and removal is slated for Python 3.14:

  - `ast.Num`

  - `ast.Str`

  - `ast.Bytes`

  - `ast.NameConstant`

  - `ast.Ellipsis`

Use [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) instead. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953).)

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - Slated for removal in Python 3.14 are the child watcher classes `asyncio.MultiLoopChildWatcher`, `asyncio.FastChildWatcher`, `asyncio.AbstractChildWatcher` and `asyncio.SafeChildWatcher`. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - Also deprecated, and due to disappear in Python 3.14, are `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()`. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - When the default event loop policy's [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) method finds no current event loop and proceeds to create one, it now raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160).)

- [`email`](https://docs.python.org/3.14/library/email.html#module-email): The *isdst* parameter of [`email.utils.localtime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.localtime) is now deprecated. (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346).)

- [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) deprecated classes:

  - `importlib.abc.ResourceReader`

  - `importlib.abc.Traversable`

  - `importlib.abc.TraversableResources`

Use [`importlib.resources.abc`](https://docs.python.org/3.14/library/importlib.resources.abc.html#module-importlib.resources.abc) classes instead:

  - [`importlib.resources.abc.Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable)

  - [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources)

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

[Subject index](INDEX.md) · [Previous source section](../python-3-13/uu-through-classmethod.md) · [Next source section](itertools-through-urllib.md)
