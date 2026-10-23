# annotationlib - Limitations of the `STRING` format - Section introduction and initial examples

### Limitations of the `STRING` format

The `STRING` format sets out to approximate the annotation’s source code, yet because of how it is built it cannot always reconstruct the precise original source.

To begin with, the stringifier naturally has no way to bring back anything absent from the compiled code — comments, whitespace, parenthesization, and any operations the compiler folds away among them.

Beyond that, while the stringifier can catch nearly every operation that hinges on names resolved within some scope, it has no purchase on operations carried out entirely over constants. A consequence of this is that asking for the `STRING` format on untrusted code is unsafe: Python is expressive enough that arbitrary code execution remains reachable even without any reach into globals or builtins. As an illustration:

```pycon
>>> def f(x: (1).__class__.__base__.__subclasses__()[-1].__init__.__builtins__["print"]("Hello world")): pass
...
>>> annotationlib.get_annotations(f, format=annotationlib.Format.STRING)
Hello world
{'x': 'None'}

```

Note

As of this writing the example above does run, but it leans on implementation details and carries no promise of continuing to work down the road.

Across the assorted expression kinds Python offers, as modeled by the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module, certain ones are supported — meaning the `STRING` format can usually bring back the original source code — while others are unsupported, meaning they might yield wrong output or an outright error.

Those below are supported (now and then with caveats):

- [`ast.BinOp`](https://docs.python.org/3.14/library/ast.html#ast.BinOp)

- [`ast.UnaryOp`](https://docs.python.org/3.14/library/ast.html#ast.UnaryOp)

  - [`ast.Invert`](https://docs.python.org/3.14/library/ast.html#ast.Invert) (`~`), [`ast.UAdd`](https://docs.python.org/3.14/library/ast.html#ast.UAdd) (`+`), and [`ast.USub`](https://docs.python.org/3.14/library/ast.html#ast.USub) (`-`) all have support

  - [`ast.Not`](https://docs.python.org/3.14/library/ast.html#ast.Not) (`not`) goes unsupported

- [`ast.Dict`](https://docs.python.org/3.14/library/ast.html#ast.Dict) (save for cases that rely on `**` unpacking)

- [`ast.Set`](https://docs.python.org/3.14/library/ast.html#ast.Set)

- [`ast.Compare`](https://docs.python.org/3.14/library/ast.html#ast.Compare)

  - [`ast.Eq`](https://docs.python.org/3.14/library/ast.html#ast.Eq) and [`ast.NotEq`](https://docs.python.org/3.14/library/ast.html#ast.NotEq) both have support

  - [`ast.Lt`](https://docs.python.org/3.14/library/ast.html#ast.Lt), [`ast.LtE`](https://docs.python.org/3.14/library/ast.html#ast.LtE), [`ast.Gt`](https://docs.python.org/3.14/library/ast.html#ast.Gt), and [`ast.GtE`](https://docs.python.org/3.14/library/ast.html#ast.GtE) have support, though the operand can come out flipped

  - [`ast.Is`](https://docs.python.org/3.14/library/ast.html#ast.Is), [`ast.IsNot`](https://docs.python.org/3.14/library/ast.html#ast.IsNot), [`ast.In`](https://docs.python.org/3.14/library/ast.html#ast.In), and [`ast.NotIn`](https://docs.python.org/3.14/library/ast.html#ast.NotIn) go unsupported

- [`ast.Call`](https://docs.python.org/3.14/library/ast.html#ast.Call) (save for cases that rely on `**` unpacking)

- [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) (yet not the constant’s exact representation; escape sequences within strings, say, are dropped, and hexadecimal numbers come back as decimal)

- [`ast.Attribute`](https://docs.python.org/3.14/library/ast.html#ast.Attribute) (provided the value is not a constant)

- [`ast.Subscript`](https://docs.python.org/3.14/library/ast.html#ast.Subscript) (provided the value is not a constant)

-

[Subject index](INDEX.md) · [Previous](creating-a-custom-callable-annotate-function.md) · [Continue](ast-starred-to-ast-yieldfrom.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)
