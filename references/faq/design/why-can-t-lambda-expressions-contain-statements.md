# Why can't lambda expressions contain statements?

### Why can't lambda expressions contain statements?

Python lambda expressions can't contain statements because Python's syntactic framework has no way to manage statements embedded inside expressions. In Python, though, that's no real obstacle. In contrast to lambda forms in other languages, where they introduce capability, Python lambdas serve merely as a shorthand notation for when you're too lazy to define a function.

Functions in Python are already first class objects, and they can be declared within a local scope. So the sole upside of reaching for a lambda over a function defined locally is that you avoid having to invent a name for the function ? yet that's just a local variable to which the function object (precisely the same kind of object that a lambda expression produces) is assigned!

[Subject index](INDEX.md)
