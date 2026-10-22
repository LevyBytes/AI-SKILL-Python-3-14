# 4.2.3. Annotation scopes

### 4.2.3. Annotation scopes

[Annotations](https://docs.python.org/3.14/glossary.html#term-annotation), [type parameter lists](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) and [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statements bring in *annotation scopes*, whose behavior largely resembles that of function scopes, save for a handful of exceptions covered below.

The contexts in which annotation scopes come into play are these:

- [Function annotations](https://docs.python.org/3.14/glossary.html#term-function-annotation).

- [Variable annotations](https://docs.python.org/3.14/glossary.html#term-variable-annotation).

- Type parameter lists for [generic type aliases](https://docs.python.org/3.14/reference/compound_stmts.html#generic-type-aliases).

- Type parameter lists for [generic functions](https://docs.python.org/3.14/reference/compound_stmts.html#generic-functions). The annotations of a generic function run inside the annotation scope, though its defaults and decorators do not.

- Type parameter lists for [generic classes](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes). The base classes and keyword arguments of a generic class run inside the annotation scope, though its decorators do not.

- The bounds, constraints, and default values for type parameters (lazily evaluated).

- The value of type aliases (lazily evaluated).

The ways in which annotation scopes part company with function scopes are these:

- Annotation scopes can reach their enclosing class namespace. When an annotation scope sits directly inside a class scope — or inside another annotation scope that itself sits directly inside a class scope — the code in that annotation scope may use names the class scope defines, just as though it ran straight inside the class body. Contrast this with ordinary functions defined inside classes, which have no access to names defined in the class scope.

- Expressions within annotation scopes are not allowed to contain [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield), `yield from`, [`await`](https://docs.python.org/3.14/reference/expressions.html#await), or [`:=`](https://docs.python.org/3.14/reference/expressions.html#grammar-token-python-grammar-assignment_expression) expressions. (Other scopes nested inside the annotation scope do permit these expressions.)

- Names that an annotation scope defines cannot be rebound by [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statements in inner scopes. That applies only to type parameters, since no other syntactic element capable of appearing inside annotation scopes can bring in new names.

- Annotation scopes do carry an internal name, but that name does not show up in the [qualified name](https://docs.python.org/3.14/glossary.html#term-qualified-name) of objects defined within the scope. Rather, the [`__qualname__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__qualname__) of such objects reads as though the object had been defined in the enclosing scope.

Added in version 3.12: The arrival of annotation scopes in Python 3.12 came by way of [**PEP 695**](https://peps.python.org/pep-0695/).

Changed in version 3.13: Type parameter defaults, brought in by [**PEP 696**](https://peps.python.org/pep-0696/), now make use of annotation scopes too.

Changed in version 3.14: Annotations themselves now rely on annotation scopes as well, per the specification in [**PEP 649**](https://peps.python.org/pep-0649/) and [**PEP 749**](https://peps.python.org/pep-0749/).

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Owning language section](binding-of-names.md) · [Previous source section](resolution-of-names.md) · [Following source section](lazy-evaluation.md)
