# struct — Functions and Exceptions

### Functions and Exceptions

This module supplies the exception and functions listed below:

`*exception *struct.error`

This exception gets raised in assorted situations; its argument is a string explaining the problem.

`struct.pack(*format*, *v1*, *v2*, *...*)`

Hand back a bytes object holding the values *v1*, *v2*, … packed in line with the format string *format*. Whatever arguments you pass have to line up precisely with what the format calls for.

`struct.pack_into(*format*, *buffer*, *offset*, *v1*, *v2*, *...*)`

Take the values *v1*, *v2*, …, pack them per the format string *format*, and deposit those packed bytes into the writable buffer *buffer* beginning at the spot *offset*. Be aware that *offset* is not optional.

`struct.unpack(*format*, *buffer*)`

Pull values out of the buffer *buffer* (assumed to have been built by `pack(format, ...)`) following the format string *format*. You always get a tuple back, even when it holds a single element. In bytes, the buffer’s length has to equal exactly what the format demands, which `calcsize()` reports.

`struct.unpack_from(*format*, */*, *buffer*, *offset=0*)`

Pull values out of *buffer* beginning at the position *offset*, in accordance with the format string *format*. You always get a tuple back, even for a single element. Counting from *offset*, the buffer must contain at least as many bytes as the format requires, which `calcsize()` reports.

`struct.iter_unpack(*format*, *buffer*)`

Step through the buffer *buffer* unpacking it piece by piece per the format string *format*. What you receive is an iterator that pulls equal-sized chunks off the buffer until nothing is left. In bytes, the buffer length has to be an exact multiple of what the format needs, which `calcsize()` reports.

Every step of the iteration produces a tuple matching the format string.

Added in version 3.4.

`struct.calcsize(*format*)`

Hand back how big the struct is — and therefore how large the bytes object that `pack(format, ...)` builds will be — for the format string *format*.

[Subject index](INDEX.md) · [Previous](struct-interpret-bytes-as-packed-binary-data.md) · [Continue](format-strings.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
