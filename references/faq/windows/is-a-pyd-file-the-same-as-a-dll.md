# Is a `*.pyd` file the same as a DLL?

### Is a `*.pyd` file the same as a DLL?

Indeed, .pyd files are dll's, though a handful of distinctions apply. Where you possess a DLL by the name `foo.pyd`, it is obliged to contain a function `PyInit_foo()`. You may then put “import foo” in Python, whereupon Python hunts for foo.pyd (along with foo.py, foo.pyc) and, upon locating it, tries to invoke `PyInit_foo()` so as to initialize it. You refrain from linking your .exe against foo.lib, since doing so would oblige Windows to insist the DLL be present.

Keep in mind that foo.pyd is searched for along PYTHONPATH, which differs from the path Windows consults when seeking foo.dll. On top of that, foo.pyd does not have to be there for your program to run, while a dll you linked your program against would be mandatory. Naturally, foo.pyd is mandatory whenever you intend to write `import foo`. Within a DLL, linkage gets stated in the source code via `__declspec(dllexport)`. Within a .pyd, linkage is laid out through a list of the functions on offer.

[Subject index](INDEX.md)
