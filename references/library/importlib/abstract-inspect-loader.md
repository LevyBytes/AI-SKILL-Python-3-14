# importlib: `importlib.abc.InspectLoader`, `get_code()`, `is_package()`, `exec_module()`, `load_module()`

*class *importlib.abc.InspectLoader

An abstract base class for a [loader](https://docs.python.org/3.14/glossary.html#term-loader) that provides the optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol meant for loaders that inspect modules.

 get_code(*fullname*)

Hand back the code object for a module, or `None` where the module has no code object (which is the situation, for example, with a built-in module). When the loader is unable to locate the module that was requested, raise an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError).

Note

A default implementation of the method exists, yet overriding it where you can is advisable for the sake of performance.

Changed in version 3.4: This is no longer abstract; a concrete version now ships.

 *abstractmethod *get_source(*fullname*)

>

An abstract method that yields a module's source. What comes back is a text string built with [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines), where each recognized line separator is converted into `'\n'` characters. Where no source can be had ? a built-in module, say ? `None` comes back. Raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) if the loader cannot find the module specified.

Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) instead of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

 is_package(*fullname*)

An optional method that yields a true value when the module is a package and a false value otherwise. [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is raised if the [loader](https://docs.python.org/3.14/glossary.html#term-loader) cannot find the module.

Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) instead of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

 *static *source_to_code(*data*, *path='&lt;string&gt;'*)

Create a code object from Python source.

For the *data* argument, anything the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) function accepts will do (that is, a string or bytes). The *path* argument is meant to be the ?path? identifying where the source originated, which may well be an abstract notion (for example, a location within a zip file).

Once you have that code object, you can run it inside a module by calling `exec(code, module.__dict__)`.

Added in version 3.4.

Changed in version 3.5: Made the method static.

 exec_module(*module*)

Implementation of `Loader.exec_module()`.

Added in version 3.4.

 load_module(*fullname*)

Implementation of `Loader.load_module()`.

Deprecated since version 3.4, will be removed in version 3.15: reach for `exec_module()` in its place.

[Subject index](INDEX.md) · [Previous](importlib-abc-resourceloader-class.md) · [Continue](importlib-abc-executionloader-class.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
