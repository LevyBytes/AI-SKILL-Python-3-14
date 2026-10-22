# contextlib: `contextlib.nullcontext()`

contextlib.nullcontext(*enter_result=None*)

Hands back a context manager whose [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) returns *enter_result* while doing nothing else. Its purpose is to substitute for a context manager that may or may not be present, for instance:

```python
def myfunction(arg, ignore_exceptions=False):
    if ignore_exceptions:
        # Use suppress to ignore all exceptions.
        cm = contextlib.suppress(Exception)
    else:
        # Do not ignore any exceptions, cm has no effect.
        cm = contextlib.nullcontext()
    with cm:
        # Do something

```

Here is a sample that leans on *enter_result*:

```python
def process_file(file_or_path):
    if isinstance(file_or_path, str):
        # If string, open file
        cm = open(file_or_path)
    else:
        # Caller is responsible for closing file
        cm = nullcontext(file_or_path)

    with cm as file:
        # Perform processing on the file

```

Equally, it can stand in for [asynchronous context managers](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers):

```python
async def send_http(session=None):
    if not session:
        # If no http session, create it with aiohttp
        cm = aiohttp.ClientSession()
    else:
        # Caller is responsible for closing the session
        cm = nullcontext(session)

    async with cm as session:
        # Send http requests with session

```

Added in version 3.7.

Changed in version 3.10: [asynchronous context manager](https://docs.python.org/3.14/glossary.html#term-asynchronous-context-manager) support was added.

[Subject index](INDEX.md) · [Previous](contextlib-closing-to-contextlib-aclosing.md) · [Continue](contextlib-suppress-to-contextlib-redirect-stdout.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)
