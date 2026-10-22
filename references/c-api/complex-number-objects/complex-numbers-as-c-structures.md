# complex number objects C API: Complex C structure pass-by-value contract

### Complex Numbers as C Structures

Keep in mind that the functions taking these structures as parameters and giving them back as results operate *by value*, never by dereferencing them through pointers. That holds true everywhere across the API.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](complex-number-objects.md) · [Following source contract](py-complex-to-py-c-pow.md)
