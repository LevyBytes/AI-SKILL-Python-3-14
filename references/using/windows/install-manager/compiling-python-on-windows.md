# 4.10. Compiling Python on Windows

### 4.10. Compiling Python on Windows

Should you wish to build CPython on your own, the very first step is obtaining the [source](https://www.python.org/downloads/source/). You may either download the source of the most recent release or simply pull a fresh [checkout](https://devguide.python.org/setup/#get-the-source-code).

Within the source tree sit a build solution and project files for Microsoft Visual Studio, the compiler that produces the official Python releases. You will find these files in the `PCbuild` directory.

Refer to `PCbuild/readme.txt` for an overview of the build process.

When it comes to extension modules, see [Building C and C++ Extensions on Windows](https://docs.python.org/3.14/extending/windows.html#building-on-windows).

[Subject index](INDEX.md) · [Previous source section](cx-freeze.md) · [Following source section](../legacy-installer/the-full-installer.md)
