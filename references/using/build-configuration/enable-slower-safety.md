# --enable-slower-safety

--enable-slower-safety

Switch on the compiler options [recommended by OpenSSF](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md) on security grounds that do carry overhead. Leave this option off and CPython is compiled without those safety options that cost performance. Turn it on and CPython gets compiled with the options shown below.

These compiler options get switched on by `--enable-slower-safety`:

- [-D_FORTIFY_SOURCE=3](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#fortify-sources-for-unsafe-libc-usage-and-buffer-overflows): Harden sources through compile-time and run-time checks targeting unsafe libc use and buffer overflows.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](disable-safety.md) · [Following source section](macos-options.md)
