# inspect / Classes and functions: `inspect.getclasstree()`, `inspect.getfullargspec()`, `FullArgSpec()`, `inspect.getargvalues()`, `inspect.formatargvalues()`, `inspect.getmro()`, `inspect.getcallargs()`, `inspect.getclosurevars()`, `inspect.unwrap()`

### Classes and functions

 inspect.getclasstree(*classes*, *unique=False*)

Organize the supplied list of classes into a hierarchy of nested lists. Wherever a nested list shows up, it holds classes derived from the class whose entry sits right before that list. Every entry is a 2-tuple pairing a class with a tuple of its base classes. When the *unique* argument is true, the returned structure contains exactly one entry per class in the supplied list. If not, classes that use multiple inheritance, along with their descendants, will show up more than once.

 inspect.getfullargspec(*func*)

Fetch the names and default values for a Python function's parameters. A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) comes back:

`FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)`

*args* lists the positional parameter names. *varargs* gives the name of the `*` parameter, or `None` when arbitrary positional arguments aren't taken. *varkw* gives the name of the `**` parameter, or `None` when arbitrary keyword arguments aren't taken. *defaults* is an *n*-tuple holding the default argument values that line up with the final *n* positional parameters, or `None` whenever no such defaults exist. *kwonlyargs* lists the keyword-only parameter names in declaration order. *kwonlydefaults* is a dictionary that maps parameter names drawn from *kwonlyargs* to the default values applied when no argument is given. *annotations* is a dictionary that maps parameter names to annotations. The dedicated key `"return"` carries the function's return value annotation (should one exist).

Keep in mind that `signature()` along with Signature Object furnish the recommended API for introspecting callables, and they cover extra behaviours (such as positional-only arguments) that crop up now and then in extension module APIs. This function lives on mainly to serve code that has to stay compatible with the Python 2 `inspect` module API.

Changed in version 3.4: This function now builds on `signature()`, yet it continues to disregard `__wrapped__` attributes and, for bound methods, keeps the already bound first parameter in the signature output.

Changed in version 3.6: Python 3.5 had documented this method as deprecated in favour of `signature()`, but that call was undone so as to bring back a clearly supported standard interface for single-source Python 2/3 code moving off the legacy `getargspec()` API.

Changed in version 3.7: Only as of version 3.7 did Python explicitly promise to keep the declaration order of keyword-only parameters, though this ordering had in fact always held in Python 3.

 inspect.getargvalues(*frame*)

Fetch details about the arguments handed into a given frame. A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `ArgInfo(args, varargs, keywords, locals)` comes back. *args* lists the argument names. *varargs* and *keywords* hold the names of the `*` and `**` arguments, or `None`. *locals* holds that frame's locals dictionary.

Note

This function was inadvertently marked as deprecated in Python 3.5.

 inspect.formatargvalues(*args*[, *varargs*, *varkw*, *locals*, *formatarg*, *formatvarargs*, *formatvarkw*, *formatvalue*])

Render a tidy argument spec out of the four values that `getargvalues()` returns. The format* arguments are the matching optional formatting functions invoked to convert names and values into strings.

Note

This function was inadvertently marked as deprecated in Python 3.5.

 inspect.getmro(*cls*)

Yield a tuple of class cls's base classes, cls itself included, ordered by method resolution order. No class shows up more than once in this tuple. Bear in mind that the method resolution order hinges on cls's type. Barring a very peculiar user-defined metatype, cls will be the tuple's first element.

 inspect.getcallargs(*func*, */*, **args*, ***kwds*)

Bind *args* and *kwds* onto the argument names of the Python function or method *func*, as though it had been invoked with them. For bound methods, also bind the first argument (typically named `self`) to the connected instance. A dict comes back, mapping the argument names (including the names of the `*` and `**` arguments, if present) to their values drawn from *args* and *kwds*. Should *func* be invoked incorrectly — that is, any time `func(*args, **kwds)` would throw because the signature is incompatible — the raised exception matches that one in type and bears the same or a comparable message. For instance:

```pycon
>>> from inspect import getcallargs
>>> def f(a, b=1, *pos, **named):
...     pass
...
>>> getcallargs(f, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
True
>>> getcallargs(f, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
True
>>> getcallargs(f)
Traceback (most recent call last):
...
TypeError: f() missing 1 required positional argument: 'a'

```

Added in version 3.2.

Deprecated since version 3.5: Use `Signature.bind()` and `Signature.bind_partial()` instead.

 inspect.getclosurevars(*func*)

Fetch the mapping of external name references inside a Python function or method *func* onto their present values. A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `ClosureVars(nonlocals, globals, builtins, unbound)` comes back. *nonlocals* ties referenced names to lexical closure variables, *globals* ties them to the function's module globals, and *builtins* ties them to the builtins reachable from the function body. *unbound* gathers the names the function references that stayed entirely unresolvable against the present module globals and builtins.

[`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised if *func* is not a Python function or method.

Added in version 3.3.

 inspect.unwrap(*func*, ***, *stop=None*)

Fetch the object that *func* wraps. It walks the chain of `__wrapped__` attributes and gives back the chain's final object.

*stop* is an optional callback that takes an object from the wrapper chain as its only argument and lets the unwrapping halt early should the callback return a true value. When the callback yields no true value at all, you get back the chain's final object as usual. To illustrate, `signature()` relies on this to halt unwrapping once any object along the chain carries a defined `__signature__` attribute.

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised if a cycle is encountered.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](bound-signature-arguments-and-defaults.md) · [Continue](inspect-get-annotations.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md)
