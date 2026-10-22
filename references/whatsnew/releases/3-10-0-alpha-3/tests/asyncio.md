# Python 3.10.0 alpha 3 / tests / asyncio

[bpo-42553](https://bugs.python.org/issue?@action=redirect&bpo=42553): Resolve a `test_asyncio.test_call_later()` race condition: avoid gauging asyncio performance inside the `call_later()` unit test. That test had been failing at random on the CI.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
