# operator: Power, sequence, item-access and length-hint operators

`operator.pow(*a*, *b*)`

 `operator.__pow__(*a*, *b*)`

Return `a ** b`.

 `operator.rshift(*a*, *b*)`

 `operator.__rshift__(*a*, *b*)`

Return `a >> b`.

 `operator.sub(*a*, *b*)`

 `operator.__sub__(*a*, *b*)`

Return `a - b`.

 `operator.truediv(*a*, *b*)`

 `operator.__truediv__(*a*, *b*)`

Give back `a / b`, so that 2/3 comes out as .66 instead of 0. People also call this “true” division.

 `operator.xor(*a*, *b*)`

 `operator.__xor__(*a*, *b*)`

Return `a ^ b`.

Operations which work with sequences (some of them with mappings too) include:

 `operator.concat(*a*, *b*)`

 `operator.__concat__(*a*, *b*)`

Return `a + b` for *a* and *b* sequences.

 `operator.contains(*a*, *b*)`

 `operator.__contains__(*a*, *b*)`

Return the outcome of the test `b in a`. Note the reversed operands.

 `operator.countOf(*a*, *b*)`

Return the number of occurrences of *b* in *a*.

 `operator.delitem(*a*, *b*)`

 `operator.__delitem__(*a*, *b*)`

Remove the value of *a* at index *b*.

 `operator.getitem(*a*, *b*)`

 `operator.__getitem__(*a*, *b*)`

Return the value of *a* at index *b*.

 `operator.indexOf(*a*, *b*)`

Return the index of the first of occurrence of *b* in *a*.

 `operator.setitem(*a*, *b*, *c*)`

 `operator.__setitem__(*a*, *b*, *c*)`

Set the value of *a* at index *b* to *c*.

 `operator.length_hint(*obj*, *default=0*)`

Give back an approximate length for the object *obj*. It first attempts the real length, falls back to an estimate via [`object.__length_hint__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__length_hint__), and as a last resort yields the default value.

Added in version 3.4.

The following operation works with callables:

[Subject index](INDEX.md) · [Previous](operator-add-to-operator-pos.md) · [Continue](operator-call-to-operator-attrgetter.md) · [Owning module, declaration or section: operator](operator-lt-to-operator-abs.md)
