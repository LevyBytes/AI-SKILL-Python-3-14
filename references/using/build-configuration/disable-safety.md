# --disable-safety

--disable-safety

Switch off the compiler options [recommended by OpenSSF](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md) on security grounds that carry no performance cost. Leave this option off and CPython gets compiled with those safety options at no speed penalty. Turn it on and CPython is compiled without the options shown below.

These compiler options get switched off by `--disable-safety`:

- [-fstack-protector-strong](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#enable-run-time-checks-for-stack-based-buffer-overflows): Switch on run-time checks guarding against stack-based buffer overflows.

- [-Wtrampolines](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#enable-warning-about-trampolines-that-require-executable-stacks): Switch on warnings covering trampolines that need executable stacks.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](with-ssl-default-suites-python-openssl-string.md) · [Following source section](enable-slower-safety.md)
