# 3.3.3.5. Executing the class body

#### 3.3.3.5. Executing the class body

Running the class body is (roughly) like calling `exec(body, globals(), namespace)`. What sets it apart from a normal [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) call is that lexical scoping lets the class body (and any methods within it) refer to names from the surrounding and enclosing scopes whenever the class definition sits inside a function.

Yet even with the class definition nested inside a function, methods declared within the class still cannot view names declared at class scope. You reach class variables through the first parameter of an instance or class method, or through the implicit lexically scoped `__class__` reference covered in the following section.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](preparing-the-class-namespace.md) · [Following source section](creating-the-class-object.md)
