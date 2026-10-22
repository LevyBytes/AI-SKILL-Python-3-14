# What's New In Python 3.7 / contextvars — asyncio, contextvars, decimal

A fresh [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars) module, paired with a group of [new C APIs](https://docs.python.org/3.14/c-api/contextvars.html#contextvarsobjects), brings *context variables* to the language. In concept, context variables resemble thread-local storage. The difference from TLS is that context variables behave correctly under asynchronous code.

Both the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) and [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) modules were reworked so they rely on and accommodate context variables natively. Notably, the live decimal context is held in a context variable now, so decimal arithmetic picks up the right context even within asynchronous code.

See also

[**PEP 567**](https://peps.python.org/pep-0567/) ? Context Variables

PEP written and implemented by Yury Selivanov

[Subject index](INDEX.md) · [Next source section](dataclasses.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](other-language-changes.md) · [Preceding release/subject continuation](other-language-changes.md)
