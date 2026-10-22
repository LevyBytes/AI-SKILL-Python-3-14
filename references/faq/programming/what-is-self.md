# What is self?

### What is self?

Self is just the customary label given to a method’s first parameter. If a method is written as `meth(self, a, b, c)`, you invoke it as `x.meth(a, b, c)` for some instance `x` of the class where the definition lives; inside, the method behaves as though it were invoked as `meth(x, a, b, c)`.

See also [Why must ‘self’ be used explicitly in method definitions and calls?](https://docs.python.org/3.14/faq/design.html#why-self).

[Subject index](INDEX.md)
