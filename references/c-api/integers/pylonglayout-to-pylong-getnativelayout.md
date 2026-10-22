# integers C API: `PyLongLayout`, `PyLong_GetNativeLayout()`

<a id="export-api"></a>

Export API: Added in version 3.14.

struct PyLongLayout

The layout of a “digits” array (the GMP terminology for these is “limbs”), employed to capture the absolute value of arbitrary precision integers.

Call `PyLong_GetNativeLayout()` to obtain the native layout of Python [`int`](https://docs.python.org/3.14/library/functions.html#int) objects, which is what gets used internally once an integer's absolute value is “big enough”.

Have a look as well at [`sys.int_info`](https://docs.python.org/3.14/library/sys.html#sys.int_info), which surfaces comparable information from within Python.

 uint8_t bits_per_digit

The count of bits in each digit. A 15 bit digit, for instance, means the meaningful information sits in bits 0-14.

 uint8_t digit_size

The size of a digit measured in bytes. A 15 bit digit, for instance, calls for no fewer than 2 bytes.

 int8_t digits_order

Digits order:

- `1` for most significant digit first

- `-1` for least significant digit first

 int8_t digit_endianness

Digit endianness:

- `1` for most significant byte first (big endian)

- `-1` for least significant byte first (little endian)

 const PyLongLayout *PyLong_GetNativeLayout(void)

Obtain the native layout belonging to Python [`int`](https://docs.python.org/3.14/library/functions.html#int) objects.

See the `PyLongLayout` structure.

You are not to call this function ahead of Python initialization or once Python finalization has happened. The layout it returns stays valid right up until Python is finalized. Since that layout holds identical across every Python sub-interpreter inside a process, you are free to cache it.

[Subject index](INDEX.md) · [Following source contract](pylongexport-to-pylong-freeexport.md)
