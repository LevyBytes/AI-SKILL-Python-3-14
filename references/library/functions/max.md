# max

max(*iterable*, */*, ***, *key=None*)

 max(*iterable*, */*, ***, *default*, *key=None*)

 max(*arg1*, *arg2*, */*, **args*, *key=None*)

Yield the largest item out of an iterable, or the largest among two or more arguments.

When a single positional argument is supplied, it ought to be an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable). The largest item within the iterable comes back. When two or more positional arguments are supplied, the largest among the positional arguments comes back.

Two optional keyword-only arguments exist. The *key* argument names a one-argument ordering function resembling the one used by [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort). The *default* argument names an object to hand back should the supplied iterable be empty. Should the iterable be empty while *default* goes unsupplied, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised.

When several items tie for maximal, the function hands back whichever was met first. This lines up with other sort-stability preserving tools like `sorted(iterable, key=keyfunc, reverse=True)[0]` and `heapq.nlargest(1, iterable, key=keyfunc)`.

Changed in version 3.4: Added the *default* keyword-only parameter.

Changed in version 3.8: The *key* can be `None`.

[Builtin task index](INDEX.md).
