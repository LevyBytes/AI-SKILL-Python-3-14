# Python 3.9.0 alpha 1 / tests / threads and concurrency

[bpo-37278](https://bugs.python.org/issue?@action=redirect&bpo=37278): Repair test_asyncio ProactorLoopCtrlC: join the thread so a running thread is not leaked and a reference is not leaked.

[bpo-35998](https://bugs.python.org/issue?@action=redirect&bpo=35998): Repair a race condition within test_asyncio.test_start_tls_server_1(). Formerly a race existed between the test main() function, which swaps the protocol, and the test ServerProto protocol, which sends ANSWER as soon as it receives HELLO. From now on only the test main() function handles sending data, and ServerProto stops sending any.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
