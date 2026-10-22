# Compilation and Linkage

### 1.5. Compilation and Linkage

Two further steps remain before your new extension is usable: compiling it and linking it into the Python system. If dynamic loading is your approach, the specifics may vary with the dynamic-loading style your system follows; see the chapters on building extension modules (chapter [Building C and C++ Extensions](https://docs.python.org/3.14/extending/building.html#building)) plus the extra material that applies only to building on Windows (chapter [Building C and C++ Extensions on Windows](https://docs.python.org/3.14/extending/windows.html#building-on-windows)) for additional details on this.

Should dynamic loading be unavailable to you, or should you wish to make your module a lasting piece of the Python interpreter, you will need to alter the configuration setup and rebuild the interpreter. Fortunately that’s very easy on Unix: simply drop your file (`spammodule.c`, say) into the `Modules/` directory of an unpacked source distribution, and add a line describing your file to the file `Modules/Setup.local`:

```sh
spam spammodule.o

```

then rebuild the interpreter by running **make** from the toplevel directory. You can run **make** in the `Modules/` subdirectory as well, but first you have to rebuild `Makefile` there by running ‘**make** Makefile’. (That step is needed each time you alter the `Setup` file.)

If your module depends on extra libraries to link against, list them on the line in the configuration file too, for example:

```sh
spam spammodule.o -lX11

```

[Subject index](INDEX.md) · [Previous source section](module-embedding-and-interpreter-support.md) · [Next source section](calling-python-functions-from-c.md)
