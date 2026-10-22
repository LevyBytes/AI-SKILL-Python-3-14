# symtable / Examining Symbol Tables: Symbol scope, annotation and comprehension classification

*class *symtable.Symbol

A single `SymbolTable` entry that maps to one identifier found in the source. Its constructor is not part of the public interface.

 get_name()

Hands back the name of the symbol.

 is_referenced()

Yields `True` when the symbol sees use within its block.

 is_imported()

Yields `True` when an import statement brought the symbol into being.

 is_parameter()

Yields `True` when the symbol happens to be a parameter.

 is_type_parameter()

Yields `True` when the symbol happens to be a type parameter.

Added in version 3.14.

 is_global()

Yields `True` when the symbol is global.

 is_nonlocal()

Yields `True` when the symbol is nonlocal.

 is_declared_global()

Yields `True` when a global statement declares the symbol global.

 is_local()

Yields `True` when the symbol is local to its own block.

 is_annotated()

Yields `True` when the symbol carries an annotation.

Added in version 3.6.

 is_free()

Yields `True` when the symbol is referenced inside its block yet never assigned to there.

 is_free_class()

Yields *True* when a class-scoped symbol counts as free as seen from within a method.

Take the example below:

```python
def f():
    x = 1  # function-scoped
    class C:
        x = 2  # class-scoped
        def method(self):
            return x

```

Here the class-scoped symbol `x` reads as free when viewed from `C.method`, which is why that method yields *1* at runtime rather than *2*.

Added in version 3.14.

 is_assigned()

Yields `True` when the symbol gets assigned to within its block.

 is_comp_iter()

Yields `True` when the symbol serves as a comprehension iteration variable.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](symtable-class-class-to-symtable-class-get-methods.md) · [Continue](symtable-symbol-is-comp-cell-to-symtable-symbol-get-namespace.md) · [Owning module, declaration or section: symtable](symtable-access-to-the-compiler-s-symbol-tables.md) · [Owning module, declaration or section: Examining Symbol Tables](symtable-symboltabletype-class.md)
