# What's New In Python 3.6 / PEP 525: Asynchronous Generators

### PEP 525: Asynchronous Generators

[**PEP 492**](https://peps.python.org/pep-0492/) brought native coroutines plus the `async` / `await` grammar into Python 3.5. One conspicuous shortcoming of that 3.5 work was the inability to combine `await` with `yield` inside one function body. Python 3.6 removes the barrier, so you can now write *asynchronous generators*:

```python
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

```

This new grammar yields code that is both quicker and tighter.

See also

[**PEP 525**](https://peps.python.org/pep-0525/): Asynchronous Generators

PEP written and implemented by Yury Selivanov.

[Subject index](INDEX.md) · [Previous source section](pep-515-underscores-in-numeric-literals.md) · [Next source section](pep-530-asynchronous-comprehensions.md) · [Release/subject declaration](summary-release-highlights.md)
