# Python 3.13.0 alpha 1 / core and builtins / way inline cache entries initialized changed cache entry jump backward

[gh-108488](https://github.com/python/cpython/issues/108488): The way inline cache entries are initialized was changed so the cache entry for `JUMP_BACKWARD` starts at zero rather than the `adaptive_counter_warmup()` value used for every other instruction. Uniquely among instructions, this counter counts upward from zero.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
