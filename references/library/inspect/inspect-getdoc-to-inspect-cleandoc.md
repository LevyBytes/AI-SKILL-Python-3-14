# inspect — Retrieving source code

### Retrieving source code

 inspect.getdoc(*object*)

Fetch the documentation string belonging to an object, tidied up by `cleandoc()`. Should an object lack its own documentation string while being a class, a method, a property or a descriptor, pull the documentation string from up the inheritance hierarchy. Hand back `None` when the documentation string is missing or invalid.

Changed in version 3.5: A documentation string is now inherited unless something overrides it.

 inspect.getcomments(*object*)

Hand back, as one string, whatever comment lines sit directly ahead of the object's source code (for a class, function, or method), or those at the head of the Python source file (when the object is a module). Should the object's source code be unavailable, hand back `None`. That may occur when the object was defined in C or within the interactive shell.

 inspect.getfile(*object*)

Hand back the name of the (text or binary) file where an object was defined. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) results if the object happens to be a built-in module, class, or function.

 inspect.getmodule(*object*)

Make a best guess at which module an object was defined in. Hand back `None` when the module cannot be pinned down.

 inspect.getsourcefile(*object*)

Hand back the name of the Python source file where an object was defined, or `None` when no means of locating the source can be found. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) results if the object happens to be a built-in module, class, or function.

 inspect.getsourcelines(*object*)

Hand back, for an object, a starting line number together with a list of its source lines. As the argument you may pass a module, a class, a method, a function, a traceback, a frame, or else a code object. What comes back is a list holding the lines that constitute the object, and the accompanying line number pinpoints where, within the original source file, that first line of code appeared. Should retrieval of the source code fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised. Passing a built-in module, class, or function instead triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Changed in version 3.3: [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) now gets raised in place of [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError), which these days is just an alias for it.

 inspect.getsource(*object*)

Hand back the text of an object's source code. As the argument you may pass a module, a class, a method, a function, a traceback, a frame, or else a code object. What comes back is the source code in the form of one single string. Should retrieval of the source code fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised. Passing a built-in module, class, or function instead triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Changed in version 3.3: [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) now gets raised in place of [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError), which these days is just an alias for it.

 inspect.cleandoc(*doc*)

Strip away indentation from docstrings that were indented so as to align with surrounding blocks of code.

Every bit of leading whitespace is taken off the first line. Whatever leading whitespace can be removed uniformly from the second line onward is removed. Blank lines at the start and finish are then dropped. On top of that, every tab is expanded into spaces.

[Subject index](INDEX.md) · [Previous](inspect-ismemberdescriptor.md) · [Continue](inspect-signature.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md)
