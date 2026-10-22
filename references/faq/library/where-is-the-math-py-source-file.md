# Where is the math.py (socket.py, regex.py, etc.) source file?

### Where is the math.py (socket.py, regex.py, etc.) source file?

When no source file turns up for a given module, it's probably a built-in or dynamically loaded module written in C, C++, or another compiled language. In that situation the source may be absent, or it may go by a name like `mathmodule.c`, located somewhere within a C source directory (and not on the Python Path).

Python has (at least) three categories of modules:

1.

modules written in Python (.py);

2.

modules written in C and dynamically loaded (.dll, .pyd, .so, .sl, etc);

3.

modules written in C and linked into the interpreter; for a listing of them, type:

```python
import sys
print(sys.builtin_module_names)

```

[Subject index](INDEX.md)
