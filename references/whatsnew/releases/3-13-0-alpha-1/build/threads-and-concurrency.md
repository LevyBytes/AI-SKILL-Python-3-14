# Python 3.13.0 alpha 1 / build / threads and concurrency

[gh-101538](https://github.com/python/cpython/issues/101538): Brought in experimental wasi-threads support. Takashi Yamamoto supplied the patch.

[gh-109740](https://github.com/python/cpython/issues/109740): The experimental `--disable-gil` configure flag from now on adds ?t? (standing for ?threaded?) into extension ABI tags.

[gh-108740](https://github.com/python/cpython/issues/108740): Fixed a race condition within `make regen-all`. The `deepfreeze.c` source plus the files that Argument Clinic emits are now produced or refreshed ahead of generating ?global objects?. Before this, certain identifiers might be absent depending on which order these files were generated in. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
