# Protocols

### Protocols

**Source code:** [Lib/asyncio/protocols.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/protocols.py)

---

For writing network protocols, asyncio offers a collection of abstract base classes. These classes are intended to operate alongside transports.

A subclass of one of these abstract base protocol classes can fill in any subset of the methods. Every one of them is a callback that a transport invokes when an event happens, such as the arrival of data. The matching transport is what should invoke a given base protocol method.

[Subject index](INDEX.md) · [Previous](subprocesstransport-get-pid-to-subprocesstransport-close.md) · [Continue](asyncio-baseprotocol-class.md)
