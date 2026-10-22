# ast: `ast.FunctionType`

*class *ast.FunctionType(*argtypes*, *returns*)

A stand-in for old-style type comments on functions, dating from when Python releases before 3.5 lacked support for [**PEP 484**](https://peps.python.org/pep-0484/) annotations. The node type `ast.parse()` returns whenever *mode* equals `"func_type"`.

Type comments of that sort take a form like this:

```python
def sum_two_number(a, b):
    # type: (int, int) -> int
    return a + b

```

`argtypes` is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of expression nodes.

`returns` is a single expression node.

```pycon
>>> print(ast.dump(ast.parse('(int, str) -> List[int]', mode='func_type'), indent=4))
FunctionType(
    argtypes=[
        Name(id='int', ctx=Load()),
        Name(id='str', ctx=Load())],
    returns=Subscript(
        value=Name(id='List', ctx=Load()),
        slice=Name(id='int', ctx=Load()),
        ctx=Load()))

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](ast-interactive-class.md) · [Continue](ast-constant-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Root nodes](ast-module-class.md)
