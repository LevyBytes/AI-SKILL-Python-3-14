# 3.3.10. Customizing positional arguments in class pattern matching

### 3.3.10. Customizing positional arguments in class pattern matching

When a class name appears in a pattern, positional arguments within the pattern are disallowed by default, i.e. `case MyClass(x, y)` is normally invalid lacking dedicated support in `MyClass`. To enable a pattern of that kind, the class has to define a *__match_args__* attribute.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](object-exit.md) · [Following source section](object-match-args.md)
