# Transports

### Transports

**Source code:** [Lib/asyncio/transports.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/transports.py)

---

[`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) supplies transport classes so that the many flavors of communication channel can be abstracted away.

It is always an [asyncio event loop](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop) that creates transport objects.

TCP, UDP, SSL, and subprocess pipes all have transports implemented by asyncio. Which methods a transport exposes is determined by the transport's kind.

The transport classes are [not thread safe](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-multithreading).

[Subject index](INDEX.md) · [Previous](transports-and-protocols.md) · [Continue](asyncio-basetransport-class.md)
