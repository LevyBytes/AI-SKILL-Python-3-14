# help

help()

 help(*request*)

Start the built-in help system. (This function is meant for interactive use.) When no argument is supplied, the interactive help system launches on the interpreter console. When the argument is a string, the system treats that string as the name of a module, function, class, method, keyword, or topic in the documentation, then prints a help page to the console. When the argument is any other sort of object, a help page describing that object is generated.

Be aware that a slash(/) showing up in a function's parameter list when you invoke `help()` signals that the parameters ahead of the slash are positional-only. For further detail, see [the FAQ entry on positional-only parameters](https://docs.python.org/3.14/faq/programming.html#faq-positional-only-arguments).

The [`site`](https://docs.python.org/3.14/library/site.html#module-site) module is what adds this function to the built-in namespace.

Changed in version 3.4: Owing to revisions in [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) and [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect), the signatures reported for callables have become more thorough and uniform.

[Builtin task index](INDEX.md).
