# Python 3.11.0 alpha 1 / library / removed

[bpo-43216](https://bugs.python.org/issue?@action=redirect&bpo=43216): The `@asyncio.coroutine` [decorator](https://docs.python.org/3.14/glossary.html#term-decorator), which let legacy generator-based coroutines interoperate with async/await code, was removed; `asyncio.coroutines.CoroWrapper`, used to wrap legacy coroutine objects under debug mode, is gone too. That decorator had been deprecated since Python 3.8, with removal first slated for Python 3.10. Illia Volochii wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
