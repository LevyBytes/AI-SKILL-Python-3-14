# double PyTime_AsSecondsDouble(PyTime_t t)

### Conversion functions

 double PyTime_AsSecondsDouble(PyTime_t t)

Convert a timestamp into a count of seconds expressed as a C double.

While this function never fails, bear in mind that a double offers only limited precision for large magnitudes.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytime-c-api.md) · [Previous source contract](pytime-monotonicraw-to-pytime-timeraw.md) · [Following source contract](../thread-local-storage-support/thread-local-storage-support.md)
