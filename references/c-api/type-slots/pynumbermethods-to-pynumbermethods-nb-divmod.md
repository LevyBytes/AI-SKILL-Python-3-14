# type slots C API: `PyNumberMethods`

### Number Object Structures

 type PyNumberMethods

Pointers to the functions an object relies on to carry out the number protocol are stored in this structure. Every function gets invoked by the similarly named function described in the [Number Protocol](https://docs.python.org/3.14/c-api/number.html#number) section.

The structure is defined as follows:

```c
typedef struct {
     binaryfunc nb_add;
     binaryfunc nb_subtract;
     binaryfunc nb_multiply;
     binaryfunc nb_remainder;
     binaryfunc nb_divmod;
     ternaryfunc nb_power;
     unaryfunc nb_negative;
     unaryfunc nb_positive;
     unaryfunc nb_absolute;
     inquiry nb_bool;
     unaryfunc nb_invert;
     binaryfunc nb_lshift;
     binaryfunc nb_rshift;
     binaryfunc nb_and;
     binaryfunc nb_xor;
     binaryfunc nb_or;
     unaryfunc nb_int;
     void *nb_reserved;
     unaryfunc nb_float;

     binaryfunc nb_inplace_add;
     binaryfunc nb_inplace_subtract;
     binaryfunc nb_inplace_multiply;
     binaryfunc nb_inplace_remainder;
     ternaryfunc nb_inplace_power;
     binaryfunc nb_inplace_lshift;
     binaryfunc nb_inplace_rshift;
     binaryfunc nb_inplace_and;
     binaryfunc nb_inplace_xor;
     binaryfunc nb_inplace_or;

     binaryfunc nb_floor_divide;
     binaryfunc nb_true_divide;
     binaryfunc nb_inplace_floor_divide;
     binaryfunc nb_inplace_true_divide;

     unaryfunc nb_index;

     binaryfunc nb_matrix_multiply;
     binaryfunc nb_inplace_matrix_multiply;
} PyNumberMethods;

```

Note

Both binary and ternary functions are required to inspect the type of all the operands they receive, and to carry out whatever conversions are needed (a minimum of one operand is an instance of the type being defined). When the operation has no definition for the supplied operands, binary and ternary functions are required to return `Py_NotImplemented`; should some other error happen, they are required to return `NULL` and set an exception.

Note

`NULL` is what the `nb_reserved` field should always hold. Its earlier name was `nb_long`, which got renamed in Python 3.0.1.

 binaryfunc PyNumberMethods.nb_add

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_nb_add` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 binaryfunc PyNumberMethods.nb_subtract

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_nb_subtract` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 binaryfunc PyNumberMethods.nb_multiply

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_nb_multiply` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 binaryfunc PyNumberMethods.nb_remainder

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_nb_remainder` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 binaryfunc PyNumberMethods.nb_divmod

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_nb_divmod` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[Subject index](INDEX.md) · [Previous source contract](heap-types.md) · [Following source contract](pynumbermethods-nb-power-to-pynumbermethods-nb-inplace-rshift.md)
