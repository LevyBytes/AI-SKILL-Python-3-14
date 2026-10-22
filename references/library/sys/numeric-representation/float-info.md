# sys.float_info

sys.float_info

A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying details about the float type. Its contents describe, at a low level, the precision and internal layout. Each value maps to one of the floating-point constants declared in the standard header `float.h` for the "C" language; consult section 5.2.4.2.2 of the 1999 ISO/IEC C standard [C99], "Characteristics of floating types", for the specifics.

  Attributes of the `float_info` [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple)
| attribute | float.h macro | explanation |
| --- | --- | --- |
| float_info.epsilon?? | `DBL_EPSILON` | the gap separating 1.0 from the next float above it that the type can represent. See also `math.ulp()`. |
| float_info.dig?? | `DBL_DIG` | The largest count of decimal digits a float can hold faithfully; details below. |
| float_info.mant_dig?? | `DBL_MANT_DIG` | Float precision, given as the count of base-`radix` digits making up a float's significand. |
| float_info.max?? | `DBL_MAX` | The largest positive finite float that can be represented. |
| float_info.max_exp?? | `DBL_MAX_EXP` | The greatest integer *e* for which `radix**(e-1)` remains a representable finite float. |
| float_info.max_10_exp?? | `DBL_MAX_10_EXP` | The greatest integer *e* for which `10**e` still falls among the representable finite floats. |
| float_info.min?? | `DBL_MIN` | The smallest positive *normalized* float that can be represented. To reach the tiniest positive *denormalized* float that is representable, apply `math.ulp(0.0)`. |
| float_info.min_exp?? | `DBL_MIN_EXP` | The least integer *e* for which `radix**(e-1)` qualifies as a normalized float. |
| float_info.min_10_exp?? | `DBL_MIN_10_EXP` | The least integer *e* for which `10**e` qualifies as a normalized float. |
| float_info.radix?? | `FLT_RADIX` | The radix of exponent representation. |
| float_info.rounds?? | `FLT_ROUNDS` | An integer that encodes which rounding mode governs floating-point arithmetic. It mirrors whatever the system `FLT_ROUNDS` macro held when the interpreter started: - `-1`: indeterminable - `0`: toward zero - `1`: to nearest - `2`: toward positive infinity - `3`: toward negative infinity Every other `FLT_ROUNDS` value stands for implementation-defined rounding behavior. |

One more note on the `sys.float_info.dig` attribute. Whenever `s` is a string standing for a decimal number that carries no more than `sys.float_info.dig` significant digits, parsing `s` into a float and serializing it back will reproduce a string for that very same decimal value:

```python
>>> import sys
>>> sys.float_info.dig
15
>>> s = '3.14159265358979'    # decimal string with 15 significant digits
>>> format(float(s), '.15g')  # convert to float and back -> same value
'3.14159265358979'

```

When a string carries more significant digits than `sys.float_info.dig`, however, this guarantee can fail:

```python
>>> s = '9876543211234567'    # 16 significant digits is too many!
>>> format(float(s), '.16g')  # conversion changes value
'9876543211234568'

```

[API family](INDEX.md) · [sys context index](../INDEX.md).
