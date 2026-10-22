# object.__iadd__(*self*, *other*) / object.__isub__(*self*, *other*) / object.__imul__(*self*, *other*) / object.__imatmul__(*self*, *other*) / object.__itruediv__(*self*, *other*) / object.__ifloordiv__(*self*, *other*) / object.__imod__(*self*, *other*) / object.__ipow__(*self*, *other*[, *modulo*]) / object.__ilshift__(*self*, *other*) / object.__irshift__(*self*, *other*) / object.__iand__(*self*, *other*) / object.__ixor__(*self*, *other*) / object.__ior__(*self*, *other*)

object.__iadd__(*self*, *other*)

 object.__isub__(*self*, *other*)

 object.__imul__(*self*, *other*)

 object.__imatmul__(*self*, *other*)

 object.__itruediv__(*self*, *other*)

 object.__ifloordiv__(*self*, *other*)

 object.__imod__(*self*, *other*)

 object.__ipow__(*self*, *other*[, *modulo*])

 object.__ilshift__(*self*, *other*)

 object.__irshift__(*self*, *other*)

 object.__iand__(*self*, *other*)

 object.__ixor__(*self*, *other*)

 object.__ior__(*self*, *other*)

These methods run to back the augmented arithmetic assignments (`+=`, `-=`, `*=`, `@=`, `/=`, `//=`, `%=`, `**=`, `<<=`, `>>=`, `&=`, `^=`, `|=`). Each should try to carry out the operation in-place (modifying *self*) and return the result (which may be, though need not be, *self*). When a given method is undefined, or when that method returns [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented), the augmented assignment reverts to the ordinary methods. For example, if *x* is an instance of a class carrying an `__iadd__()` method, `x += y` amounts to `x = x.__iadd__(y)` . If `__iadd__()` is missing, or if `x.__iadd__(y)` returns `NotImplemented`, then `x.__add__(y)` and `y.__radd__(x)` are considered, just as in evaluating `x + y`. Under some circumstances, augmented assignment can surface surprising errors (consult [Why does a_tuple[i] += ["item"] raise an exception when the addition works?](https://docs.python.org/3.14/faq/programming.html#faq-augmented-assignment-tuple-error)), yet this behavior is genuinely part of the data model.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-numeric-types.md) · [Previous source section](object-radd-self-and-other.md) · [Following source section](object-neg-object-pos-object-abs-object-invert.md)
