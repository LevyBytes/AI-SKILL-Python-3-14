# asyncio — Logging

### Logging

asyncio leans on the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module, routing every bit of its logging through the `"asyncio"` logger.

Its log level starts out at [`logging.INFO`](https://docs.python.org/3.14/library/logging.html#logging.INFO), and changing that is straightforward:

```python
logging.getLogger("asyncio").setLevel(logging.WARNING)

```

Because logging over a network can stall the event loop, the advice is to handle logs on a dedicated thread or rely on non-blocking IO. As one reference, consult [Dealing with handlers that block](https://docs.python.org/3.14/howto/logging-cookbook.html#blocking-handlers).

[Subject index](INDEX.md) · [Previous](running-blocking-code.md) · [Continue](detect-never-awaited-coroutines.md)
