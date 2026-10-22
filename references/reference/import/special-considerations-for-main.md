# 5.8. Special considerations for __main__

### 5.8. Special considerations for __main__

Within Python's import system the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module stands as a special case. As pointed out [elsewhere](https://docs.python.org/3.14/reference/toplevel_components.html#programs), the `__main__` module is initialized directly when the interpreter starts up, in much the way [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) and [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) are. Unlike that pair, though, it does not strictly count as a built-in module. The reason is that how `__main__` gets initialized hinges on the flags and other options used to invoke the interpreter.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](package-relative-imports.md) · [Following source section](main-spec.md)
