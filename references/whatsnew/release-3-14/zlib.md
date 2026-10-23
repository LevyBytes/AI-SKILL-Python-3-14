# What's new in Python 3.14 / zlib - zlib

### zlib

- Under Windows, the default binaries now build the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module on top of [zlib-ng](https://github.com/zlib-ng/zlib-ng). No incompatibilities are known between `zlib-ng` and the `zlib` implementation used before. The outcome should be improved performance across every compression level.

Worth flagging is that `zlib.Z_BEST_SPEED` (`1`) can yield noticeably less compression than the earlier implementation did, while also cutting the time needed to compress by a wide margin.

(Contributed by Steve Dower in [gh-91349](https://github.com/python/cpython/issues/91349).)

[Subject index](INDEX.md) · [Previous source section](uuid.md) · [Next source section](argparse.md) · [Release/subject declaration](summary-release-highlights.md)
