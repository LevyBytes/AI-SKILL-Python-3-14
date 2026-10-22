# Extending

## Extending

### Extending

The primary way to extend [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) is by authoring your own *event loop* classes. Asyncio ships helper utilities that make this work less involved.

Note

Outside parties leaning on existing asyncio internals should tread carefully: any fresh Python release is permitted to break compatibility within the *internal* portion of the API.

[Subject index](INDEX.md) · [Continue](writing-a-custom-event-loop.md)
