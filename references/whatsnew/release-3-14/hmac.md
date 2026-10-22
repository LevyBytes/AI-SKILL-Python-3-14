# What's new in Python 3.14 / hmac

### hmac

- A native HMAC implementation ([**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html)) was added, drawing on formally verified code out of the [HACL*](https://github.com/hacl-star/hacl-star/) project. Whenever the OpenSSL HMAC implementation is missing, this one serves as the fallback. (Contributed by Bénédikt Tran in [gh-99108](https://github.com/python/cpython/issues/99108).)

[Subject index](INDEX.md) · [Previous source section](heapq.md) · [Next source section](http.md) · [Release/subject declaration](summary-release-highlights.md)
