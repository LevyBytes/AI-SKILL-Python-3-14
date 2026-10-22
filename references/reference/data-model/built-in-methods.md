# 3.2.8.7. Built-in methods

#### 3.2.8.7. Built-in methods

This amounts to another guise of a built-in function, except that here an object travels to the C function as an implicit additional argument. Take `alist.append()` as an example of a built-in method, where *alist* names a list object. Here the special read-only attribute `__self__` points to the object that *alist* denotes. (That attribute carries the same meaning that it carries for `other instance methods`.)

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](built-in-functions.md) · [Following source section](classes.md)
