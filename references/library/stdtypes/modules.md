# Modules

### Modules

Attribute access is the lone special operation a module provides: `m.name`, in which *m* names a module and *name* reaches a name held in *m*’s symbol table. You may assign to module attributes. (Note that the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement, strictly speaking, is not an operation performed on a module object; `import foo` does not call for a module object named *foo* to already exist — rather, it calls for an (external) *definition* of a module named *foo* somewhere.)

[`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) is a special attribute that every module carries. It is the dictionary that holds the module’s symbol table. Editing this dictionary really does alter the module’s symbol table, yet you cannot assign straight to the `__dict__` attribute (you may write `m.__dict__['a'] = 1`, which sets `m.a` to `1`, but writing `m.__dict__ = {}` is not allowed). Editing `__dict__` directly is discouraged.

Modules compiled into the interpreter are shown like this: `<module 'sys' (built-in)>`. When loaded from a file instead, they are shown as `<module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'>`.

[Subject index](INDEX.md) · [Previous](other-built-in-types.md) · [Continue](classes-and-class-instances.md)
