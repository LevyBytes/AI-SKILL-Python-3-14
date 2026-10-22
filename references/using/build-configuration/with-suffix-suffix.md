# --with-suffix=SUFFIX

--with-suffix=SUFFIX

Assign *SUFFIX* as the suffix of the Python executable.

That suffix defaults to `.exe` under Windows and macOS (giving a `python.exe` executable), `.js` for Emscripten node, `.html` for Emscripten browser, `.wasm` on WASI, and to an empty string elsewhere (giving a `python` executable).

Changed in version 3.11: On the WASM platform the default suffix is now one among `.js`, `.html` or `.wasm`.

[Subject index](INDEX.md) · [Previous source section](enable-big-digits-15-30.md) · [Following source section](with-tzpath-list-of-absolute-paths-separated-by-pathsep.md)
