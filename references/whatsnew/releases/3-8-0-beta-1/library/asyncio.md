# Python 3.8.0 beta 1 / library / asyncio

[bpo-35545](https://bugs.python.org/issue?@action=redirect&bpo=35545): Stops asyncio from dropping IPv6 scopes during its internal hostname resolution work

[bpo-36806](https://bugs.python.org/issue?@action=redirect&bpo=36806): Bans constructing asyncio stream objects — StreamReader, StreamWriter, Process, plus their protocols — anywhere outside the asyncio package.

[bpo-36801](https://bugs.python.org/issue?@action=redirect&bpo=36801): Correctly manages the teardown of an SSL connection during the asyncio StreamWriter.drain() call.

[bpo-37028](https://bugs.python.org/issue?@action=redirect&bpo=37028): Delivers an asyncio REPL

[bpo-32528](https://bugs.python.org/issue?@action=redirect&bpo=32528): Turns asyncio.CancelledError into a BaseException.

This tackles a frequent slip among asyncio users: an “except Exception” clause that disrupts Tasks cancellation.

Alongside this change, asyncio.TimeoutError and asyncio.InvalidStateError stop inheriting from their concurrent.futures.* counterparts. Sharing an inheritance chain serves no purpose for these exceptions.

[bpo-32972](https://bugs.python.org/issue?@action=redirect&bpo=32972): Delivers `unittest.IsolatedAsyncioTestCase` as an aid for testing asyncio-based code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
