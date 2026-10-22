# object.__lt__(*self*, *other*) / object.__le__(*self*, *other*) / object.__eq__(*self*, *other*) / object.__ne__(*self*, *other*) / object.__gt__(*self*, *other*) / object.__ge__(*self*, *other*)

object.__lt__(*self*, *other*)

 object.__le__(*self*, *other*)

 object.__eq__(*self*, *other*)

 object.__ne__(*self*, *other*)

 object.__gt__(*self*, *other*)

 object.__ge__(*self*, *other*)

These constitute the so-called “rich comparison” methods. Operator symbols line up with method names this way: `x<y` calls `x.__lt__(y)`, `x<=y` calls `x.__le__(y)`, `x==y` calls `x.__eq__(y)`, `x!=y` calls `x.__ne__(y)`, `x>y` calls `x.__gt__(y)`, and `x>=y` calls `x.__ge__(y)`.

A rich comparison method is allowed to return the singleton [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) whenever it lacks an implementation of the operation for a particular pair of arguments. By convention, a successful comparison yields `False` and `True`. These methods may, however, return any value at all, so when the comparison operator appears in a Boolean context (for instance, the condition of an `if` statement), Python applies [`bool()`](https://docs.python.org/3.14/library/functions.html#bool) to the value to settle whether the outcome is true or false.

By default, `object` realizes `__eq__()` via `is`, yielding [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) whenever a comparison turns out false: `True if x is y else NotImplemented`. As for `__ne__()`, by default it defers to `__eq__()` and flips the outcome unless that outcome happens to be `NotImplemented`. No further implied relationships hold among the comparison operators or their default implementations; for instance, the truth of `(x<y or x==y)` carries no implication that `x<=y`. To derive ordering operations automatically from one root operation, consult [`functools.total_ordering()`](https://docs.python.org/3.14/library/functools.html#functools.total_ordering).

By default, the [`object`](https://docs.python.org/3.14/library/functions.html#object) class furnishes implementations that align with [Value comparisons](https://docs.python.org/3.14/reference/expressions.html#expressions-value-comparisons): equality is judged by object identity, and order comparisons raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Each default method might produce these outcomes outright, though it may instead return [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented).

Consult the paragraph covering `__hash__()` for several key notes about building [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) objects that support custom comparison operations and serve as dictionary keys.

These methods have no swapped-argument variants (for use when the left argument cannot support the operation but the right one can); instead, `__lt__()` and `__gt__()` mirror each other, `__le__()` and `__ge__()` mirror each other, while `__eq__()` and `__ne__()` mirror themselves. Should the operands have differing types, and the right operand’s type be a direct or indirect subclass of the left operand’s type, the right operand’s reflected method takes precedence; otherwise the left operand’s method takes precedence. Virtual subclassing is not taken into account.

Whenever no suitable method returns anything besides [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented), the `==` and `!=` operators fall back to `is` and `is not`, respectively.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Previous source section](object-format.md) · [Following source section](object-hash.md)
