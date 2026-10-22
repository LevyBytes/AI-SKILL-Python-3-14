# sys._emscripten_info

sys._emscripten_info

A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying details about the environment on the *wasm32-emscripten* platform. This named tuple is provisional and could change down the line.

 _emscripten_info.emscripten_version

Emscripten version as tuple of ints (major, minor, micro), e.g. `(3, 1, 8)`.

 _emscripten_info.runtime

Runtime string, e.g. browser user agent, `'Node.js v14.18.2'`, or `'UNKNOWN'`.

 _emscripten_info.pthreads

`True` if Python is compiled with Emscripten pthreads support.

 _emscripten_info.shared_memory

`True` if Python is compiled with shared memory support.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Emscripten.

Added in version 3.11.

[API family](INDEX.md) · [sys context index](../INDEX.md).
