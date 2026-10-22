# Python 2.3 changes: Set subset and superset example

```python
>>> S1 = sets.Set([1,2,3])
>>> S2 = sets.Set([2,3])
>>> S2.issubset(S1)
True
>>> S1.issubset(S2)
False
>>> S1.issuperset(S2)
True
>>>

```

See also

[**PEP 218**](https://peps.python.org/pep-0218/) - Adding a Built-In Set Object Type

The PEP came from Greg V. Wilson. The implementation was the work of Greg V. Wilson, plus Alex Martelli and GvR.

[Subject index](INDEX.md) · [Previous source section](standard-set-type.md) · [Next source section](pep-255-simple-generators.md) · [Release/subject declaration](standard-set-type.md)
