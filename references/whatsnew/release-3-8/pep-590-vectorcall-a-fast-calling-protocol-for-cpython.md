# What’s New In Python 3.8 / PEP 590: Vectorcall: a fast calling protocol for CPython

### PEP 590: Vectorcall: a fast calling protocol for CPython

[The Vectorcall Protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall) joins the Python/C API. Its purpose is to give an official shape to optimizations that several classes were already enjoying. Any [static type](https://docs.python.org/3.14/c-api/typeobj.html#static-types) that implements a callable is free to adopt the protocol.

For now it remains provisional. The plan is to promote it to fully public status in Python 3.9.

A complete write-up appears in [**PEP 590**](https://peps.python.org/pep-0590/).

(Jeroen Demeyer, Mark Shannon and Petr Viktorin contributed this in [bpo-36974](https://bugs.python.org/issue?@action=redirect&bpo=36974).)

[Subject index](INDEX.md) · [Previous source section](pep-587-python-initialization-configuration.md) · [Next source section](pickle-protocol-5-with-out-of-band-data-buffers.md) · [Release/subject declaration](assignment-expressions.md)
