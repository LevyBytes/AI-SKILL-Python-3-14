# 4.2.1. Binding of names

### 4.2. Naming and binding

### 4.2.1. Binding of names

*Names* point at objects. Name binding operations are what bring names into being.

Names are bound by the following constructs:

- formal parameters to functions,

- class definitions,

- function definitions,

- assignment expressions,

- [targets](https://docs.python.org/3.14/reference/simple_stmts.html#assignment) that are identifiers if occurring in an assignment:

  - [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop header,

  - following `as` within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause, an [`except*`](https://docs.python.org/3.14/reference/compound_stmts.html#except-star) clause, or inside the as-pattern when matching structural patterns,

  - in a capture pattern in structural pattern matching

- [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statements.

- [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statements.

- [type parameter lists](https://docs.python.org/3.14/reference/compound_stmts.html#type-params).

When the `import` statement takes the form `from ... import *`, it binds every name the imported module defines, save for those that start with an underscore. Only at the module level may this form appear.

For these purposes, a target appearing in a [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) statement also counts as bound (even though what it really does is unbind the name).

Every assignment or import statement sits inside a block — one defined by a class or function definition, or else the module level itself (the top-level code block).

When a name is bound inside a block, it becomes a local variable of that block, except where it is declared [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) or [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global). A name bound at the module level becomes a global variable. (For the module code block, the variables count as both local and global.) A variable that a code block uses without defining is a [free variable](https://docs.python.org/3.14/glossary.html#term-free-variable).

Wherever a name shows up in the program text, it points at the *binding* of that name set up by the name resolution rules that follow.

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Previous source section](structure-of-a-program.md) · [Following source section](resolution-of-names.md)
