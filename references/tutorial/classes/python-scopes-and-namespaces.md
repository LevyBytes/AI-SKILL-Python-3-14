# 9.2. Python Scopes and Namespaces

### 9.2. Python Scopes and Namespaces

Before I bring in classes, I need to explain a few things about how scoping works in Python. Namespace handling is where class definitions perform some clever maneuvers, and grasping how scopes and namespaces operate is essential to seeing the full picture. As it happens, understanding this topic pays off for any seasoned Python developer.

We'll start with a few definitions.

A *namespace* maps names onto objects. At present most namespaces are built as Python dictionaries, though that fact is usually invisible (apart from its effect on performance) and could be altered down the road. Among the namespaces you'll meet are: the collection of built-in names (which holds functions like [`abs()`](https://docs.python.org/3.14/library/functions.html#abs) along with the names of built-in exceptions); the global names within a module; and the local names during a function call. In one sense, an object's set of attributes constitutes a namespace too. The key point to grasp about namespaces is that names sitting in distinct namespaces have no connection whatsoever; for example, two separate modules can each declare a function `maximize` with no clash — callers of those modules just have to qualify it with the module's name.

On a related note, I apply the term *attribute* to any name that comes after a dot — so, in the expression `z.real`, `real` counts as an attribute of the object `z`. To be precise, name references inside modules are attribute references: in `modname.funcname`, `modname` is a module object while `funcname` is one of its attributes. Here it turns out there is a clean correspondence between the module's attributes and the global names declared in that module: both sit in one shared namespace! [1]

An attribute might be read-only, or it might be writable. When it is writable, you can assign to it. Module attributes can be written to: writing `modname.the_answer = 42` is permitted. Writable attributes can additionally be removed with the [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) statement. As an example, `del modname.the_answer` strips the attribute `the_answer` off the object that `modname` names.

Different namespaces come into being at different times and persist for differing spans. The namespace holding the built-in names springs up as the Python interpreter boots and is never torn down. A module's global namespace appears when the module's definition gets read; module namespaces normally survive right up to interpreter shutdown. Statements run by the interpreter's top-level invocation, whether fed from a script file or typed interactively, belong to a module named [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__), and so they receive their own global namespace. (Strictly, the built-in names reside in a module as well, one called [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins).)

A function's local namespace is born when the function is invoked, and it disappears once the function returns or throws an exception that the function itself doesn't catch. (In reality, forgetting is a more accurate description of what takes place.) Naturally, every recursive call gets a local namespace all its own.

A *scope* denotes a textual stretch of a Python program in which a namespace is reachable without qualification. "Directly accessible" means that an unqualified mention of a name will try to locate that name within the namespace.

Even though scopes are fixed statically, their use is dynamic. At any given moment while code runs, between 3 and 4 nested scopes have their namespaces directly reachable:

- the innermost scope, consulted first, holds the local names

- the scopes belonging to any surrounding functions, scanned beginning with the closest enclosing scope, hold names that are neither local nor global

- the next-to-last scope holds the current module's global names

- the outermost scope (scanned last) is the namespace that holds built-in names

When a name is declared global, every reference and assignment to it goes straight to the next-to-last scope that holds the module's global names. To re-bind variables that live outside the innermost scope, you can apply the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement; absent a nonlocal declaration, those variables are read-only (writing to one merely produces a *new* local variable in the innermost scope and leaves the outer variable of the same name untouched).

Typically the local scope points at the local names of whatever function is (textually) current. Beyond any function, the local scope points at the very namespace the global scope does: the module's namespace. A class definition introduces an additional namespace into the local scope.

It helps to recognize that scopes are settled by the text itself: a function defined in a module has that module's namespace as its global scope, regardless of where the function is invoked from or under which alias. The hunt for names, by contrast, happens dynamically, while the program runs — yet the language is drifting toward resolving names statically, at "compile" time, so you shouldn't lean on dynamic name resolution! (Indeed, local variables are settled statically already.)

One peculiar trait of Python is that — when no [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) or [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement applies — assignments to names always land in the innermost scope. Assignments don't copy any data; they merely bind names onto objects. Deletion behaves identically: the statement `del x` takes away the binding of `x` from whatever namespace the local scope points at. Truthfully, every operation that brings in new names works through the local scope: in particular, [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statements and function definitions bind the module name or function name within the local scope.

The [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) statement serves to declare that certain variables belong to the global scope and ought to be re-bound there; the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement declares that certain variables belong to an enclosing scope and ought to be re-bound there.

[Subject index](INDEX.md) · [Previous source section](a-word-about-names-and-objects.md) · [Following source section](scopes-and-namespaces-example.md)
