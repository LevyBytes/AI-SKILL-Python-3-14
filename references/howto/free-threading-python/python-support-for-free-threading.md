# Python support for free threading

# Free Threading Python

### Python support for free threading

As of the 3.13 release, CPython ships a variant of the interpreter known as [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading), in which the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) (GIL) no longer applies. With this mode, threads can run simultaneously across the machine's CPU cores, so the full compute capacity of the hardware becomes usable. Plenty of code gains nothing for free here, yet anything written deliberately around threads should see better throughput on systems with several cores.

Certain packages from outside the standard library — most notably those that bundle an [extension module](https://docs.python.org/3.14/glossary.html#term-extension-module) — might not yet function under a free-threaded build and can switch the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) back on.

What follows here lays out what free threading means in practice when you write Python. For guidance on authoring C extensions that work with the free-threaded interpreter, consult [C API Extension Support for Free Threading](https://docs.python.org/3.14/howto/free-threading-extensions.html#freethreading-extensions-howto).

See also

[**PEP 703**](https://peps.python.org/pep-0703/) – Making the Global Interpreter Lock Optional in CPython, which gives a broad account of free-threaded Python.

[Subject index](INDEX.md) · [Following source context](installation.md)
