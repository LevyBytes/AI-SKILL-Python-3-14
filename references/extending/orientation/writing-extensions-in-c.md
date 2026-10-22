# Writing Extensions in C++

### 1.11. Writing Extensions in C++

You can certainly build extension modules in C++, subject to a few caveats. Should the main program (that is, the Python interpreter) be compiled and linked through the C compiler, you cannot rely on global or static objects that have constructors. Linking the main program with the C++ compiler removes that obstacle. Any function the Python interpreter will call — module initialization functions above all — needs an `extern "C"` declaration. There is no need to wrap the Python header files in `extern "C" {...}`, since they already adopt that form whenever the symbol `__cplusplus` is set (which every modern C++ compiler does).

[Subject index](INDEX.md) · [Previous source section](null-pointer-reference-counting.md) · [Next source section](providing-a-c-api-for-an-extension-module-and-py-mod-exec.md)
