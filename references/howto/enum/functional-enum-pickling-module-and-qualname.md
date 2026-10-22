# Functional Enum creation and pickling module/qualname requirements

### Functional API

Because the [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) class is callable, it offers this functional API:

```python
>>> Animal = Enum('Animal', 'ANT BEE CAT DOG')
>>> Animal
<enum 'Animal'>
>>> Animal.ANT
<Animal.ANT: 1>
>>> list(Animal)
[<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]

```

This API behaves much like [`namedtuple`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple). When calling [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum), the first argument supplies the enumeration's name.

For the second argument you give the *source* of the enumeration's member names. It may be a string of names separated by whitespace, a sequence of names, a sequence of 2-tuples holding key/value pairs, or a mapping (such as a dictionary) from names to values. Those final two forms let you pin arbitrary values to the enumeration; the rest auto-assign rising integers beginning at 1 (pass the `start` parameter to choose a different first value). What comes back is a fresh class derived from [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum). Put differently, the `Animal` assignment above amounts to:

```python
>>> class Animal(Enum):
...     ANT = 1
...     BEE = 2
...     CAT = 3
...     DOG = 4
...

```

We default the first number to `1` rather than `0` because `0` reads as `False` in a boolean context, whereas every enum member should normally evaluate to `True`.

Pickling enums built through the functional API can get fiddly, since frame stack internals are leaned on to guess which module is creating the enumeration (so, for instance, it breaks if a helper in another module does the work, and it may also fall over on IronPython or Jython). The fix is to state the module name outright like this:

```python
>>> Animal = Enum('Animal', 'ANT BEE CAT DOG', module=__name__)

```

Warning

When `module` goes unspecified and Enum can't work it out for itself, the resulting Enum members can't be unpickled; so that failures stay near their origin, pickling is switched off.

In certain situations the new pickle protocol 4 also depends on [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#type.__qualname__) pointing at the spot where pickle can locate the class. For instance, if the class were exposed inside class SomeData at global scope:

```python
>>> Animal = Enum('Animal', 'ANT BEE CAT DOG', qualname='SomeData.Animal')

```

[Subject index](INDEX.md) · [Complete Enum functional signature, parameters and start version note](functional-enum-signature-and-start-parameter.md) · [Previous source context](pickling.md) · [Following source context](functional-enum-signature-and-start-parameter.md)
