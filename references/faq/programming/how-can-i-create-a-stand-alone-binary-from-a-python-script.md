# How can I create a stand-alone binary from a Python script?

### How can I create a stand-alone binary from a Python script?

Compiling Python down to C code isn't required when your only goal is a self-contained program that people can download and launch without first installing the Python distribution. A variety of tools figure out which modules a program needs and bundle those modules together with a Python binary, yielding one executable.

One option is the freeze tool, shipped within the Python source tree at [Tools/freeze](https://github.com/python/cpython/tree/3.14/Tools/freeze). It transforms Python byte code into C arrays; using a C compiler, you can fold every one of your modules into a fresh program that then links against the standard Python modules.

The way it operates is by recursively scanning your source for import statements (in either form) and hunting for the modules along the standard Python path and within the source directory (for built-in modules). Next it converts the bytecode of modules authored in Python into C code (array initializers convertible into code objects via the marshal module) and produces a tailored config file holding only those built-in modules the program genuinely uses. Finally, it compiles that generated C code and links it together with the remainder of the Python interpreter to build a self-contained binary that behaves exactly as your script does.

The packages below can assist in producing console and GUI executables:

- [Nuitka](https://nuitka.net/) (Cross-platform)

- [PyInstaller](https://pyinstaller.org/) (Cross-platform)

- [PyOxidizer](https://pyoxidizer.readthedocs.io/en/stable/) (Cross-platform)

- [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/) (Cross-platform)

- [py2app](https://github.com/ronaldoussoren/py2app) (macOS only)

- [py2exe](https://www.py2exe.org/) (Windows only)

[Subject index](INDEX.md)
