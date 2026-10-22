# Built-in Functions

eval(*source*, */*, *globals=None*, *locals=None*)

Parameters:

- **source** ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) | [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects)) – A Python expression.

- **globals** ([`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) | `None`) – The global namespace (default: `None`).

- **locals** ([mapping](https://docs.python.org/3.14/glossary.html#term-mapping) | `None`) – The local namespace (default: `None`).

Returns:

The result of the evaluated expression.

Raises:

Syntax errors are reported as exceptions.

Warning

Arbitrary code gets run by this function. Feeding it untrusted input that came from a user opens the door to security vulnerabilities.

The *source* argument is parsed and then evaluated as a Python expression (in formal terms, a condition list), drawing on the *globals* and *locals* mappings to serve as the global and local namespace. Should the *globals* dictionary exist yet hold no entry for the key `__builtins__`, then before *source* gets parsed a reference to the built-in module [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins)'s dictionary is placed under that key. You can override `__builtins__` to limit or alter which names are reachable, yet this is **not** a security mechanism: the code being run retains full access to every builtin. When the *locals* mapping is left out, its default becomes the *globals* dictionary. With both mappings absent, evaluation of the source happens against the *globals* and *locals* of the surrounding context where `eval()` was invoked. Keep in mind that *eval()* can reach the [nested scopes](https://docs.python.org/3.14/glossary.html#term-nested-scope) (non-locals) of the enclosing context only when they are already referenced within the scope from which `eval()` runs (for instance, through a [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement).

Example:

```python
>>> x = 1
>>> eval('x+1')
2

```

You may also use this function to run arbitrary code objects (for example, ones built by `compile()`). For that, hand it a code object rather than a string. When the code object was compiled using `'exec'` for the *mode* argument, the value `eval()` returns will be `None`.

Hints: the `exec()` function handles dynamic execution of statements. The `globals()` and `locals()` functions hand back the current global and local dictionary, respectively, and these can be handy to pass along for `eval()` or `exec()` to use.

When the supplied source comes in as a string, leading and trailing spaces along with tabs are stripped away.

Refer to [`ast.literal_eval()`](https://docs.python.org/3.14/library/ast.html#ast.literal_eval) for a function that evaluates strings holding expressions made up of literals only.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `exec`, passing the code object along as its argument. Events tied to code compilation can be raised too.

Changed in version 3.13: It is now permitted to supply the *globals* and *locals* arguments by keyword.

Changed in version 3.13: The behavior of the default *locals* namespace was revised, matching what is described for the `locals()` builtin.

[Subject index](INDEX.md) · [Previous](enumerate.md) · [Continue](INDEX.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
