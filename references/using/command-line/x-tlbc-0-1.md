# -X tlbc=*0,1*

- `-X tlbc=*0,1*` turns on (1, the default) or turns off (0) thread-local bytecode within builds set up with [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil). Turning it off additionally turns off the specializing interpreter. Refer also to `PYTHON_TLBC`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](x-context-aware-warnings-0-1.md) · [Following source section](x-arbitrary-values-and-option-history.md)
