# 6.2.3.2. String literal concatenation

#### 6.2.3.2. String literal concatenation

You may place several string or bytes literals next to one another ? even mixing quoting styles ? and the result means exactly what their concatenation would mean:

```python
>>> "hello" 'world'
"helloworld"

```

Since this behavior is defined at the syntactic level, it applies to literals alone. When you need to join string expressions at run time, reach for the ?+? operator:

```python
>>> greeting = "Hello"
>>> space = " "
>>> name = "Blaise"
>>> print(greeting + space + name)   # not: print(greeting space name)
Hello Blaise

```

Within a single concatenation you can freely intermix raw strings, triple-quoted strings, and formatted string literals. Here is an example:

```python
>>> "Hello" r', ' f"{name}!"
"Hello, Blaise!"

```

This capability comes in handy for cutting down on backslashes, for breaking lengthy strings across several lines neatly, or even for attaching comments to individual pieces of a string. Take this case:

```python
re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"   # letter, digit or underscore
          )

```

Bytes literals, though, can be joined only with other byte literals ? never with string literals of any sort. In the same way, a template string literal can only be joined with other template string literals:

```python
>>> t"Hello" t"{name}!"
Template(strings=('Hello', '!'), interpolations=(...))

```

Formally:

```text

strings: (STRING | fstring)+ | tstring+
```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](literals.md) · [Previous source section](literals-and-object-identity.md) · [Following source section](parenthesized-forms.md)
