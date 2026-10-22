# Python 3.8.0 beta 1 / core and builtins / memory and lifetimes

[bpo-27987](https://bugs.python.org/issue?@action=redirect&bpo=27987): On 64-bit platforms pymalloc now hands back memory blocks aligned to 16 bytes rather than 8 bytes, matching the x86-64 ABI. Modern compilers lean on that alignment with growing frequency. Inada Naoki wrote the patch.

[bpo-37029](https://bugs.python.org/issue?@action=redirect&bpo=37029): Releasing a huge population of tiny objects once cost time quadratic in arena count, since a linear scan kept `obmalloc.c`’s roster of usable arenas ordered by their free-memory-pool counts. That ordering no longer needs any scan, so the worst case is now linear in arena count. Where this is plainly noticeable — usually above 100 thousand tiny objects living at once — the memory-release time can fall dramatically.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
