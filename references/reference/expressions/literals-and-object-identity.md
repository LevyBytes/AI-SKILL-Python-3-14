# 6.2.3.1. Literals and object identity

#### 6.2.3.1. Literals and object identity

Because every literal maps to an immutable data type, the value of the resulting object matters more than its identity. Evaluating literals that share a value more than once ? whether from one spot in the source text or from separate spots ? might yield the very same object, or might instead yield distinct objects that happen to share that value.

CPython implementation detail

To illustrate, under CPython *small* integers sharing a value evaluate to one and the same object:

```python
>>> x = 7
>>> y = 7
>>> x is y
True

```

Larger integers, by contrast, evaluate to separate objects:

```python
>>> x = 123456789
>>> y = 123456789
>>> x is y
False

```

Future CPython releases may behave differently here. Notably, the cutoff dividing ?small? from ?large? integers has shifted before.

Comparing literals with `is` makes CPython raise a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning):

```python
>>> x = 7
>>> x is 7
<input>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
True

```

For further detail, see [When can I rely on identity tests with the is operator?](https://docs.python.org/3.14/faq/programming.html#faq-identity-with-is).

Although [template strings](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings) themselves are immutable, they can hold references to mutable objects through their [`Interpolation`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation) values. Within this section, two t-strings count as having the ?same value? when their structure matches and the *identity* of their values matches as well.

**CPython implementation detail:** At present, every time a template string is evaluated it yields a fresh object.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](literals.md) · [Previous source section](literals.md) · [Following source section](string-literal-concatenation.md)
