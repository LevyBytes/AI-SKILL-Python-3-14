# Imports, request data, formatter and context variables

### Use of `contextvars`

Beginning with Python 3.7, the [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars) module has offered context-local storage that serves the needs of both [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) and [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) processing. As a result, this form of storage is generally a better choice than thread-locals. The example that follows demonstrates how, within a multi-threaded setting, logs can be enriched with contextual information — for example, request attributes processed by web applications.

By way of illustration, suppose you run several web applications, each one independent of the others but executing inside the same Python process and drawing on a library they all share. How might each of these applications maintain its own log, where every logging message originating in the library (and in other request-processing code) is steered into the right application's log file, while also embedding extra contextual details in the log such as client IP, HTTP request method and client username?

Let's suppose the library can be stood in for by the code below:

```python
# webapplib.py
import logging
import time

logger = logging.getLogger(__name__)

def useful():
    # Just a representative event logged from the library
    logger.debug('Hello from webapplib!')
    # Just sleep for a bit so other threads get to run
    time.sleep(0.01)

```

We can stand in for the several web applications using two straightforward classes, `Request` and `WebApp`. These mimic the way real threaded web applications operate — each request gets handled on its own thread:

Open the [complete example modules](../../examples/request-context-logging/INDEX.md) for the complete definitions, imports and entrypoint.

[Subject index](INDEX.md) · [Coupled example phase](context-injecting-filter-and-whole-webapp-class.md) · [Coupled example phase](request-simulation-thread-joins-and-entry-point.md) · [Context-injecting filter and whole WebApp class](context-injecting-filter-and-whole-webapp-class.md) · [Request simulation, thread joins and entry point](request-simulation-thread-joins-and-entry-point.md) · [Previous source context](using-filters-to-impart-contextual-information.md) · [Following source context](context-injecting-filter-and-whole-webapp-class.md)
