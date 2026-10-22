# ctypes: `ctypes.Array`, `ctypes.ARRAY()`

### Arrays and pointers

`*class *ctypes.Array(**args*)`

The abstract base class underlying arrays.

The preferred route to a concrete array type is to multiply some `ctypes` data type by a non-negative integer. As an alternative, you may subclass this type and declare the `_length_` and `_type_` class variables. You read and write array elements with ordinary subscript and slice access; a slice read yields an object that is *not* itself an `Array`.

Arrays are [generic](https://docs.python.org/3.14/library/typing.html#generics) with respect to the type held in their elements.

`_length_`

A positive integer that states how many elements the array holds. Subscripts that fall out of range raise an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError). This value is what [`len()`](https://docs.python.org/3.14/library/functions.html#len) reports.

`_type_`

States the type of every element held in the array.

Constructors of an Array subclass take positional arguments, which seed the elements one after another.

`ctypes.ARRAY(*type*, *length*)`

Build an array. The same as `type * length`, in which *type* is a `ctypes` data type and *length* an integer.

This function is [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated), with multiplication now preferred. There is no intention of removing it.

[Subject index](INDEX.md) · [Previous](structured-data-types-ctypes-cfield.md) · [Continue](ctypes-pointer-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
