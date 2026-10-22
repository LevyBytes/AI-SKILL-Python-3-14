# macOS

### macOS

Recent versions of macOS enjoy full support.

macOS <= 10.8

Under macOS 10.6, 10.7 and 10.8, the default event loop relies on [`selectors.KqueueSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.KqueueSelector), which on those versions has no support for character devices. You can configure the [`SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) by hand to rely on [`SelectSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.SelectSelector) or [`PollSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.PollSelector) so that character devices work on those older macOS versions. Example:

```python
import asyncio
import selectors

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

```

[Subject index](INDEX.md) · [Previous](subprocess-support-on-windows.md) · [Continue](../asyncio-policy/policies.md)
