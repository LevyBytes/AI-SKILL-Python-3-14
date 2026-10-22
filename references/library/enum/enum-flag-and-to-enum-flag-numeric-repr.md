# enum.Flag: `__and__()`, `__xor__()`, `__invert__()`, `_numeric_repr_()`

__and__(*self*, *other*)

Yields the present flag binary and’ed together with other:

```python
>>> purple & white
<Color.RED|BLUE: 5>
>>> purple & Color.GREEN
<Color: 0>

```

 __xor__(*self*, *other*)

Yields the present flag binary xor’ed together with other:

```python
>>> purple ^ white
<Color.GREEN: 2>
>>> purple ^ Color.GREEN
<Color.RED|GREEN|BLUE: 7>

```

 __invert__(*self*)

Yields every flag in *type(self)* that is absent from *self*:

```python
>>> ~white
<Color: 0>
>>> ~purple
<Color.GREEN: 2>
>>> ~Color.RED
<Color.GREEN|BLUE: 6>

```

 _numeric_repr_()

The function tasked with formatting whatever unnamed numeric values are left over. By default it uses the value’s repr; frequent alternatives are [`hex()`](https://docs.python.org/3.14/library/functions.html#hex) and [`oct()`](https://docs.python.org/3.14/library/functions.html#oct).

Note

Pairing `auto` with `Flag` produces integers that are powers of two, beginning at `1`.

Changed in version 3.11: For zero-valued flags, the *repr()* has been altered. These days it reads:

```python
>>> Color(0)
<Color: 0>

```

[Subject index](INDEX.md) · [Previous](enum-flag-class-to-enum-flag-or.md) · [Continue](enum-intflag-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.Flag](enum-flag-class-to-enum-flag-or.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
