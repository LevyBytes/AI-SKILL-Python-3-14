# Python 3.13.0 alpha 1 / tests / repaired test socket test hmac sha1 under fips mode

[gh-109396](https://github.com/python/cpython/issues/109396): Repaired `test_socket.test_hmac_sha1()` under FIPS mode. Adopt a longer key, because FIPS mode demands no fewer than 112 bits. That earlier key carried just 32 bits. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
