# 6.2.2.1. Private name mangling

#### 6.2.2.1. Private name mangling

Should an identifier appear in the text of a class definition starting with at least two underscores while not finishing with two or more underscores, that class treats it as a *private name*.

See also

The [class specifications](https://docs.python.org/3.14/reference/compound_stmts.html#class).

To be more exact, private names get rewritten into an expanded form before the compiler produces code for them. Truncation that depends on the implementation can occur whenever the rewritten name exceeds 255 characters.

How the identifier is used syntactically has no bearing on the transformation; nonetheless, only these private identifiers undergo mangling:

- Every name serving as a variable that is written to or read from, and every name of an attribute being looked up.

That said, the [`__name__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__name__) attribute belonging to nested functions, classes, and type aliases is left untouched.

- The name given to an imported module, such as `__spam` within `import __spam`. When that module belongs to a package (that is, a dot appears in its name), no mangling occurs ? for instance, `__foo` in `import __foo.bar` stays as written.

- The name of an imported member, for example `__f` in `from spam import __f`.

Here is how the transformation rule works:

- The class name ? its leading underscores stripped and one leading underscore added back ? is placed ahead of the identifier. So `__spam` written inside a class called `Foo`, `_Foo`, or `__Foo` becomes `_Foo__spam`.

- When nothing but underscores make up the class name, the transformation leaves the name unchanged: `__spam` appearing inside a class called `_` or `__` stays as it is.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](identifiers.md) · [Previous source section](identifiers.md) · [Following source section](literals.md)
