# 4.2.5. Builtins and restricted execution

### 4.2.5. Builtins and restricted execution

**CPython implementation detail:** `__builtins__` is something users ought to leave alone; it is purely an implementation detail. A user who wants to override values in the builtins namespace should [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) the [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) module and alter its attributes as appropriate.

The builtins namespace tied to a code block's execution is in fact located by looking up the name `__builtins__` within that block's global namespace; the result should be a dictionary or a module (and in the module case its dictionary is what gets used). The default is this: inside the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module, `__builtins__` is the built-in module [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins); inside any other module, `__builtins__` stands as an alias for the dictionary of the `builtins` module itself.

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Owning language section](binding-of-names.md) · [Previous source section](lazy-evaluation.md) · [Following source section](interaction-with-dynamic-features.md)
