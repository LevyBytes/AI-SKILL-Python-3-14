# Builtin Iterator Types

### Builtin Iterator Types

The following iteration types are bundled into Python's C API yet expose no extra functions. Their listing here is for the sake of completeness.

| C type | Python type |
| --- | --- |
| PyTypeObject PyEnum_Type * Part of the Stable ABI.* | `enumerate` |
| PyTypeObject PyFilter_Type * Part of the Stable ABI.* | `filter` |
| PyTypeObject PyMap_Type * Part of the Stable ABI.* | `map` |
| PyTypeObject PyReversed_Type * Part of the Stable ABI.* | `reversed` |
| PyTypeObject PyZip_Type * Part of the Stable ABI.* | `zip` |

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyseqiter-type-to-pycalliter-new.md) · [Previous source contract](pyrange-type-to-pyrange-check.md) · [Following source contract](pybytearrayiter-type-to-pyodictiter-type.md)
