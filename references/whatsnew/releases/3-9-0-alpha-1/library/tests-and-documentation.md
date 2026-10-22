# Python 3.9.0 alpha 1 / library / tests and documentation

[bpo-37428](https://bugs.python.org/issue?@action=redirect&bpo=37428): For client connections, SSLContext.post_handshake_auth = True no longer turns on the SSL_VERIFY_POST_HANDSHAKE verify flag. The documentation states the option is disregarded for clients, yet OpenSSL quietly switches on cert chain validation once that flag is present.

[bpo-37328](https://bugs.python.org/issue?@action=redirect&bpo=37328): `HTMLParser.unescape` has been dropped. It carried no documentation and had been deprecated as far back as Python 3.4.

[bpo-37531](https://bugs.python.org/issue?@action=redirect&bpo=37531): Running ?python3 -m test -jN ?timeout=TIMEOUT? will now terminate any worker process whose runtime exceeds *TIMEOUT* seconds.

[bpo-38136](https://bugs.python.org/issue?@action=redirect&bpo=38136): The call count and await count of AsyncMock are now tracked by two separate counters. The await count now increments only once a coroutine has actually been awaited rather than merely called, and the reverse holds as well. The accompanying documentation was updated.

[bpo-18578](https://bugs.python.org/issue?@action=redirect&bpo=18578): Joannah Nanjekye renamed and documented `test.bytecode_helper` as `test.support.bytecode_helper`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
