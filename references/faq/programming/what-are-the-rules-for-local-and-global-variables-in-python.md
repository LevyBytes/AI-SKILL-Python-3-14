# What are the rules for local and global variables in Python?

### What are the rules for local and global variables in Python?

Within Python, a variable that a function only reads is implicitly global. When a value gets assigned to a variable anywhere inside the function's body, that variable is taken to be local unless it has been explicitly declared global.

This is a touch surprising at first, but a brief reflection clears it up. For one thing, demanding [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) for assigned variables sets up a guard against unintended side-effects. For another, were `global` mandatory for every global reference, you'd be reaching for `global` constantly. Each reference to a built-in function or to a piece of an imported module would have to be declared global. That noise would undermine how useful the `global` declaration is for pinpointing side-effects.

[Subject index](INDEX.md)
