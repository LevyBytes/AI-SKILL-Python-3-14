# 4.2.2. Embedding Python

### 4.2.2. Embedding Python

Applications written in native code frequently need some kind of scripting language, and the embedded Python distribution can serve that role. Usually most of the application is native code, while a portion either calls `python.exe` or uses `python3.dll` directly. In either situation, unpacking the embedded distribution into a subdirectory of the application installation suffices to supply a loadable Python interpreter.

Just as with the application use, packages may be installed anywhere, since there is a chance to set search paths before the interpreter initializes. Apart from that, there is no real difference between using the embedded distribution and a regular installation.

[Subject index](INDEX.md) · [Previous source section](python-application.md) · [Following source section](the-nuget-org-packages.md)
