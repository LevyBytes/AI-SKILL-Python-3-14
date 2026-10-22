# exec

exec(*source*, */*, *globals=None*, *locals=None*, ***, *closure=None*)

Warning

Arbitrary code gets run by this function. Feeding it untrusted input that came from a user opens the door to security vulnerabilities.

Dynamic execution of Python code is what this function provides. *source* needs to be either a string or a code object. When it is a string, that string gets parsed as a suite of Python statements and is then run (assuming no syntax error arises). [1] When it is a code object, it just gets executed. Across every case, whatever code runs has to qualify as valid file input (consult the section [File input](https://docs.python.org/3.14/reference/toplevel_components.html#file-input) within the Reference Manual). Note that the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal), [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield), and [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statements cannot appear outside function definitions, and that holds even inside code handed to the `exec()` function. The value returned is `None`.

In every case, omitting the optional parts means the code runs within the current scope. When *globals* alone is supplied, it has to be a dictionary (and not a dictionary subclass), and it serves for both the global and the local variables. When both *globals* and *locals* are supplied, they back the global and local variables, respectively. If you give it, *locals* may be any mapping object. Bear in mind that at module level, globals and locals refer to the very same dictionary.

Note

When `exec` receives two distinct objects as *globals* and *locals*, the code runs as though it were placed inside a class definition. As a result, any functions and classes defined within the executed code won't reach variables assigned at the top level (because those “top level” variables behave like class variables within a class definition).

Should the *globals* dictionary lack a value under the key `__builtins__`, then a reference to the built-in module [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins)'s dictionary gets placed under that key. You can override `__builtins__` to limit or alter which names are reachable, yet this is **not** a security mechanism: the code being run retains full access to every builtin.

The *closure* argument provides a closure–a tuple of cellvars. It is valid solely when the *object* is a code object that holds [free (closure) variables](https://docs.python.org/3.14/glossary.html#term-closure-variable). The tuple's length has to line up precisely with the length of the code object's [`co_freevars`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_freevars) attribute.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `exec`, passing the code object along as its argument. Events tied to code compilation can be raised too.

Note

The built-in functions `globals()` and `locals()` hand back the current global and local namespace, respectively, and these can prove handy to pass along as the second and third argument to `exec()`.

Note

The default *locals* behave as laid out for the function `locals()` further below. Supply an explicit *locals* dictionary whenever you need to observe what the code did to *locals* after the function `exec()` returns.

Changed in version 3.11: Added the *closure* parameter.

Changed in version 3.13: It is now permitted to supply the *globals* and *locals* arguments by keyword.

Changed in version 3.13: The behavior of the default *locals* namespace was revised, matching what is described for the `locals()` builtin.

[Builtin task index](INDEX.md).
