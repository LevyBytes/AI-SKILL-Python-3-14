# 4.9.2. Keyword Arguments

### 4.9.2. Keyword Arguments

It’s also possible to invoke functions with [keyword arguments](https://docs.python.org/3.14/glossary.html#term-keyword-argument) written as `kwarg=value`. Consider, for example, this function:

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

```

takes one mandatory argument (`voltage`) plus three optional ones (`state`, `action`, and `type`). Any of these forms can be used to call the function:

```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

```

yet every one of the calls below would be invalid:

```python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

```

Within any call, keyword arguments always come after the positional ones. Each keyword you supply has to correspond to a parameter the function actually accepts (`actor`, for instance, is not recognized by `parrot`), though the sequence you list them in does not matter. Even mandatory parameters qualify here (`parrot(voltage=1000)` works fine as well). A single parameter can never be assigned twice. The snippet below breaks precisely because of that rule:

```python
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'

```

Should the last formal parameter take the shape `**name`, that slot collects a dictionary (consult [Mapping Types — dict](https://docs.python.org/3.14/library/stdtypes.html#typesmapping)) holding every keyword argument that did not line up with a declared parameter. You can pair it with a `*name` parameter (covered in the following subsection), which gathers a [tuple](https://docs.python.org/3.14/tutorial/datastructures.html#tut-tuples) of the positional arguments that overflow past the declared parameters. (`*name` has to appear ahead of `**name`.) Suppose we write a function such as the following:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

```

An invocation might look like the following:

```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

```

and naturally the output would be:

```none
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch

```

Observe that the sequence used when printing those keyword arguments is promised to mirror exactly how they appeared in the original call.

[Subject index](INDEX.md) · [Previous source section](default-argument-values.md) · [Following source section](special-parameters.md)
