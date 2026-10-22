# ast: `ast.dump()`, `ast.compare()`

ast.dump(*node*, *annotate_fields=True*, *include_attributes=False*, ***, *indent=None*, *show_empty=False*)

Produce a formatted dump of the tree held in *node*. Its main value is in debugging. With *annotate_fields* true (the default), the string handed back spells out both the field names and their values. With *annotate_fields* false, the result grows more compact since unambiguous field names drop out. By default, attributes like line numbers and column offsets stay out of the dump; flip *include_attributes* to true if you want them.

When *indent* is a non-negative integer or a string, the tree is pretty-printed at that indent level. A level of 0, a negative value, or `""` merely adds newlines. The default of `None` picks the one-line form. A positive integer indents by that count of spaces at each level, whereas a string *indent* (`"\t"`, for example) becomes the per-level indentation itself.

Leaving *show_empty* at its false default drops optional empty lists from what gets printed. Optional `None` values never appear regardless.

Changed in version 3.9: Added the *indent* option.

Changed in version 3.13: Added the *show_empty* option.

```pycon
>>> print(ast.dump(ast.parse("""\
... async def f():
...     await other_func()
... """), indent=4, show_empty=True))
Module(
    body=[
        AsyncFunctionDef(
            name='f',
            args=arguments(
                posonlyargs=[],
                args=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Expr(
                    value=Await(
                        value=Call(
                            func=Name(id='other_func', ctx=Load()),
                            args=[],
                            keywords=[])))],
            decorator_list=[],
            type_params=[])],
    type_ignores=[])

```

 ast.compare(*a*, *b*, */*, ***, *compare_attributes=False*)

Recursively compares two ASTs.

Whether AST attributes enter into the comparison is governed by *compare_attributes*. Left at its `False` default, attributes play no part; set otherwise, every one of them has to match. The flag is handy for asking whether two ASTs share the same structure yet diverge in whitespace or comparable particulars. Line numbers and column offsets count among these attributes.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](ast-nodetransformer-class.md) · [Continue](ast-pycf-allow-top-level-await-to-ast-pycf-type-comments.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: `ast` helpers](ast-parse.md)
