# ctypes: Structure and union layout selection

_layout_

An optional string that names the struct/union layout. At present it accepts:

- `"ms"`: the layout the Microsoft compiler (MSVC) uses. On GCC and Clang, you select this layout via `__attribute__((ms_struct))`.

- `"gcc-sysv"`: the layout GCC uses with the System V or “SysV-like” data model, as found on Linux and macOS. Under this layout, `_pack_` has to be unset or zero.

When left unset explicitly, `ctypes` falls back to a default suited to the platform conventions. That default could shift in upcoming Python releases (for instance, when a new platform receives official support, or when a discrepancy between similar platforms is discovered). For now the default will be:

- On Windows: `"ms"`

- When `_pack_` is specified: `"ms"`. (This is deprecated; refer to the `_pack_` documentation.)

- Otherwise: `"gcc-sysv"`

`_layout_` has to be defined already when `_fields_` is assigned, or it will take no effect.

Added in version 3.14.

 _anonymous_

An optional sequence naming the unnamed (anonymous) fields. `_anonymous_` has to be defined already when `_fields_` is assigned, or it will take no effect.

The fields named in this variable have to be structure or union type fields. `ctypes` will produce descriptors on the structure type that grant direct access to the nested fields, sparing you from having to create the structure or union field.

Below is an example type (Windows):

```python
class _U(Union):
    _fields_ = [("lptdesc", POINTER(TYPEDESC)),
                ("lpadesc", POINTER(ARRAYDESC)),
                ("hreftype", HREFTYPE)]

class TYPEDESC(Structure):
    _anonymous_ = ("u",)
    _fields_ = [("u", _U),
                ("vt", VARTYPE)]

```

The `TYPEDESC` structure describes a COM data type, and the `vt` field tells which of the union fields is valid. Because the `u` field is declared as an anonymous field, you can now reach the members straight off the TYPEDESC instance. `td.lptdesc` and `td.u.lptdesc` mean the same thing, but the first is quicker since it avoids creating a temporary union instance:

```python
td = TYPEDESC()
td.vt = VT_PTR
td.lptdesc = POINTER(some_type)
td.u.lptdesc = POINTER(some_type)

```

You may also define sub-subclasses of structures; they inherit the base class fields. When the subclass definition carries its own `_fields_` variable, the fields named there are appended after the base class fields.

Structure and union constructors take both positional and keyword arguments. Positional arguments initialize member fields following the same order in which they show up in `_fields_`. Keyword arguments to the constructor are read as attribute assignments, so they initialize the `_fields_` of matching name, or add new attributes for names absent from `_fields_`.

[Subject index](INDEX.md) · [Previous](ctypes-structure-class.md) · [Continue](ctypes-cfield-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: ctypes.Structure](ctypes-structure-class.md) · [Owning module, declaration or section: Structured data types](ctypes-union-class.md)
