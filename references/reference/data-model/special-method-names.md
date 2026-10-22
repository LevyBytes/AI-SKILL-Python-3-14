# 3.3. Special method names

### 3.3. Special method names

By defining methods bearing special names, a class can supply particular operations that special syntax triggers (for example arithmetic operations or subscripting and slicing). This constitutes Python’s take on *operator overloading*, letting classes specify their own behavior toward the language’s operators. As an illustration, when a class defines a method called `__getitem__()`, and `x` is an instance of that class, then `x[i]` is roughly the same as `type(x).__getitem__(x, i)`. Save where otherwise noted, trying to carry out an operation raises an exception if no suitable method has been defined (commonly [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError)).

Assigning `None` to a special method signals that the matching operation is unavailable. To illustrate, when a class assigns `None` to `__iter__()`, that class becomes non-iterable, so invoking [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) on its instances raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) (with no fallback to `__getitem__()`). [2]

When you write a class that mimics one of the built-in types, it matters that the imitation reach only as far as is sensible for the object you are modelling. As an example, certain sequences may handle the retrieval of single elements perfectly well, while pulling out a slice may not be meaningful. (The [NodeList](https://docs.python.org/3.14/library/xml.dom.html#dom-nodelist-objects) interface in the W3C’s Document Object Model serves as one such example.)

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Previous source section](class-method-objects.md) · [Following source section](object-new.md)
