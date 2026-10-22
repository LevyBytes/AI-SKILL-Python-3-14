# What's New in Python 2.5 / PEP 357: The "__index__" method

### PEP 357: The "__index__" method

The NumPy developers ran into a difficulty that could be resolved only by introducing a fresh special method, `__index__()`. With slice notation such as `[start:stop:step]`, every one of the *start*, *stop*, and *step* indexes has to be either an integer or a long integer. NumPy supplies an assortment of specialized integer types for unsigned and signed integers spanning 8, 16, 32, and 64 bits, yet nothing existed to indicate that those types were valid as slice indexes.

The already-present `__int__()` method can't simply be reused for slicing, since that method also serves to coerce things to integers. Were slicing to lean on `__int__()`, floating-point numbers would then qualify as legitimate slice indexes too, which is plainly unwanted behaviour.

Instead a brand-new special method, `__index__()`, was introduced. It accepts no arguments and hands back an integer specifying which slice index to use. As an illustration:

```python
class C:
    def __index__ (self):
        return self.value

```

What's returned has to be either a Python integer or a long integer. The interpreter verifies that the returned type is right, throwing a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when that condition isn't satisfied.

To allow C extensions to implement the protocol, a matching [`nb_index`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods.nb_index) slot was placed in the C-level [`PyNumberMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods) structure. From extension code, `PyNumber_Index(obj)` will invoke the `__index__()` function and fetch the result it produces.

See also

[**PEP 357**](https://peps.python.org/pep-0357/) - Allowing Any Object to be Used for Slicing

PEP authored and implemented by Travis Oliphant.

[Subject index](INDEX.md) · [Previous source section](pep-353-using-ssize-t-as-the-index-type.md) · [Next source section](other-language-changes-zerodict-and-is-image-file.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
