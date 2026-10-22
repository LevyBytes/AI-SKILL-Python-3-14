# What's New In Python 3.7 / PEP 539: New C API for Thread-Local Storage

### PEP 539: New C API for Thread-Local Storage

Python does ship a C API supporting thread-local storage; however, the present [Thread Local Storage (TLS) API](https://docs.python.org/3.14/c-api/tls.html#thread-local-storage-api) has relied on int for TLS keys on every platform. That has rarely caused trouble for the platforms officially supported, yet it is neither POSIX-compliant nor portable in any meaningful way.

[**PEP 539**](https://peps.python.org/pep-0539/) addresses that by adding a new [Thread Specific Storage (TSS) API](https://docs.python.org/3.14/c-api/tls.html#thread-specific-storage-api) into CPython, which replaces the older TLS API throughout the CPython interpreter and marks that older API as deprecated. Rather than int, the TSS API adopts a fresh type [`Py_tss_t`](https://docs.python.org/3.14/c-api/tls.html#c.Py_tss_t) for TSS keys — an opaque type whose definition can vary with the underlying TLS implementation. Consequently, CPython can be built on platforms whose native TLS key is declared so that it cannot be safely cast to int.

Be aware that on platforms whose native TLS key is declared so that it cannot be safely cast to int, every function of the older TLS API becomes a no-op and returns failure right away. That makes plain that the legacy API has no support on platforms where reliable use is impossible, and that adding such support is not planned.

See also

[**PEP 539**](https://peps.python.org/pep-0539/) — A New C-API for Thread-Local Storage in CPython

PEP written by Erik M. Bray; implementation by Masayuki Yamamoto.

[Subject index](INDEX.md) · [Previous source section](pep-553-built-in-breakpoint.md) · [Next source section](pep-562-customization-of-access-to-module-attributes.md) · [Release/subject declaration](summary-release-highlights.md)
