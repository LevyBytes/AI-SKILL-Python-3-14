# complex number objects C API: `Py_complex`, `_Py_c_sum()`, `_Py_c_diff()`, `_Py_c_neg()`, `_Py_c_prod()`, `_Py_c_quot()`, `_Py_c_pow()`

type Py_complex

The C structure matching the value portion of a Python complex number object. The bulk of the functions that work with complex number objects take structures of this type as their input or output values, whichever fits.

 double real

 double imag

Here is how the structure is defined:

```c
typedef struct {
    double real;
    double imag;
} Py_complex;

```

 Py_complex _Py_c_sum(Py_complex left, Py_complex right)

Hand back the sum of two complex numbers in the C `Py_complex` representation.

 Py_complex _Py_c_diff(Py_complex left, Py_complex right)

Hand back the difference of two complex numbers in the C `Py_complex` representation.

 Py_complex _Py_c_neg(Py_complex num)

Hand back the negation of the complex number *num* in the C `Py_complex` representation.

 Py_complex _Py_c_prod(Py_complex left, Py_complex right)

Hand back the product of two complex numbers in the C `Py_complex` representation.

 Py_complex _Py_c_quot(Py_complex dividend, Py_complex divisor)

Hand back the quotient of two complex numbers in the C `Py_complex` representation.

Should *divisor* be null, this method hands back zero and sets `errno` to `EDOM`.

 Py_complex _Py_c_pow(Py_complex num, Py_complex exp)

Hand back *num* raised to the power *exp* in the C `Py_complex` representation.

Should *num* be null while *exp* is not a positive real number, this method hands back zero and sets `errno` to `EDOM`.

On overflow, set `errno` to `ERANGE`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](complex-number-objects.md) · [Owning C API section and shared conditions](complex-numbers-as-c-structures.md) · [Following source contract](pycomplexobject-to-pycomplex-asccomplex.md)
