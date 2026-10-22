# Manually Un-Stringizing Stringized Annotations

### Manually Un-Stringizing Stringized Annotations

When you face annotations that might be “stringized” and you want those strings evaluated down to the Python values they stand for, by far the best course is to let [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) handle that work.

On Python 3.9 or earlier, or whenever [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) is off the table for you, you'll have to reproduce its behaviour yourself. A good idea is to study how `inspect.get_annotations()` is written in the present Python release and mirror that strategy.

Put briefly, to evaluate a stringized annotation found on some arbitrary object `o`:

- Where `o` happens to be a module, hand `o.__dict__` to [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) as its `globals`.

- Where `o` is a class, pass `sys.modules[o.__module__].__dict__` for the `globals` and `dict(vars(o))` for the `locals` in your [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) call.

- Where `o` is a callable wrapped via [`functools.update_wrapper()`](https://docs.python.org/3.14/library/functools.html#functools.update_wrapper), [`functools.wraps()`](https://docs.python.org/3.14/library/functools.html#functools.wraps), or [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial), peel it back step by step through `o.__wrapped__` or `o.func` as fits the case, until you arrive at the underlying unwrapped function.

- Where `o` is a callable yet not a class, supply [`o.__globals__`](https://docs.python.org/3.14/reference/datamodel.html#function.__globals__) for the globals in your [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) call.

Be aware, though, that [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) can't reliably convert every string used as an annotation into a Python value. In principle such a string may be any valid string at all, and there genuinely are type-hint scenarios that call for annotating with strings which by design *can't* be evaluated. Take these cases:

- [**PEP 604**](https://peps.python.org/pep-0604/) union types written with `|` in the era before Python 3.10 gained support for them.

- Definitions with no runtime role, pulled in solely while [`typing.TYPE_CHECKING`](https://docs.python.org/3.14/library/typing.html#typing.TYPE_CHECKING) holds true.

Set [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) on values like those and it will choke, raising an exception. For that reason, when you build a library API that deals with annotations, the advice is to evaluate string values only when the caller has explicitly asked for it.

[Subject index](INDEX.md) · [Previous source context](annotation-dictionaries-python-3-9-and-older.md) · [Following source context](best-practices-for-annotations-in-any-python-version.md)
